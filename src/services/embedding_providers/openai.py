import openai
from typing import List
import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from src.services.embedding_providers.base import EmbeddingProvider

logger = logging.getLogger(__name__)

class OpenAIEmbeddingProvider(EmbeddingProvider):
    def __init__(self, api_key: str, model: str):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=1, max=10),
        retry=retry_if_exception_type(
            (openai.APIError, openai.APIConnectionError, openai.RateLimitError)
        ),
        reraise=True,
    )
    async def generate_embedding(self, text: str) -> List[float]:
        try:
            max_chars = 30000
            if len(text) > max_chars:
                logger.warning(f"Text truncated from {len(text)} to {max_chars} characters")
                text = text[:max_chars]

            response = self.client.embeddings.create(
                model=self.model, input=text, encoding_format="float"
            )

            embedding = response.data[0].embedding
            logger.info(f"Generated embedding with dimension: {len(embedding)}")
            return embedding

        except (openai.APIError, openai.APIConnectionError, openai.RateLimitError) as e:
            logger.warning(f"OpenAI API error (will retry): {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to generate embedding: {e}")
            raise

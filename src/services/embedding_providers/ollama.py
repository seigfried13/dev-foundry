import ollama
from typing import List
import logging
from src.services.embedding_providers.base import EmbeddingProvider

logger = logging.getLogger(__name__)

class OllamaEmbeddingProvider(EmbeddingProvider):
    def __init__(self, model: str, ollama_url: str):
        self.model = model
        self.client = ollama.Client(host=ollama_url)

    async def generate_embedding(self, text: str) -> List[float]:
        try:
            response = self.client.embeddings(model=self.model, prompt=text)
            embedding = response["embedding"]
            logger.info(f"Generated embedding with dimension: {len(embedding)}")
            return embedding
        except Exception as e:
            logger.error(f"Failed to generate embedding with Ollama: {e}")
            raise

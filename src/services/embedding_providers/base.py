from abc import ABC, abstractmethod
from typing import List

class EmbeddingProvider(ABC):
    @abstractmethod
    async def generate_embedding(self, text: str) -> List[float]:
        pass

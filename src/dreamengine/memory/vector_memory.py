# src/dreamengine/memory/vector_memory.py

from dreamengine.memory.backends.chroma_memory import ChromaMemory
from dreamengine.memory.backends.faiss_memory import FaissMemory
from dreamengine.utils.logger import get_logger

logger = get_logger(__name__)


class VectorMemory:
    """
    A pluggable vector memory system. Wraps backend-specific logic.
    """

    def __init__(self, backend: str = "chroma"):
        self.backend = backend.lower()
        if self.backend == "chroma":
            self.engine = ChromaMemory()
        elif self.backend == "faiss":
            self.engine = FaissMemory()
        else:
            raise ValueError(f"Unsupported memory backend: {self.backend}")

        logger.info(f"VectorMemory initialized with backend: {self.backend}")

    def store(self, content: str):
        self.engine.store(content)

    def retrieve(self, query: str, top_k: int = 5):
        return self.engine.retrieve(query, top_k)

# src/dreamengine/core/kernel.py

from dreamengine.memory.vector_memory import VectorMemory
from dreamengine.llm.local_llm import LocalLLM
from dreamengine.agents.dream_agent import DreamAgent
from dreamengine.utils.logger import get_logger

logger = get_logger(__name__)


class DreamKernel:
    """
    The central controller of the DreamEngine agent.
    Orchestrates memory, LLM, agent reasoning, and hallucinated beliefs.
    """

    def __init__(self):
        self.memory = VectorMemory()
        self.llm = LocalLLM()
        self.agent = DreamAgent(self.llm, self.memory)

        logger.info("DreamKernel initialized.")

    def observe(self, input_text: str) -> str:
        """
        Simulate perception: process external input.
        """
        logger.debug(f"Observing input: {input_text}")
        self.memory.store(input_text)
        response = self.agent.respond(input_text)
        self.memory.store(response)
        return response

    def dream(self) -> str:
        """
        Simulate internal hallucinated thought.
        """
        logger.debug("Entering dream mode...")
        hallucinated_prompt = self.agent.generate_hallucination()
        hallucinated_response = self.llm.generate(hallucinated_prompt)
        self.memory.store(hallucinated_response)
        return hallucinated_response

    def reflect(self) -> str:
        """
        Simulate introspection by summarizing or altering beliefs.
        """
        logger.debug("Performing reflection...")
        return self.agent.reflect()


# Dev test hook (optional)
if __name__ == "__main__":
    kernel = DreamKernel()
    print(kernel.observe("Where am I?"))
    print(kernel.dream())
    print(kernel.reflect())

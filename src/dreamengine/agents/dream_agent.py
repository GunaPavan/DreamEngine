# src/dreamengine/agents/dream_agent.py

from dreamengine.llm.llm_orchestrator import LLMOrchestrator
from dreamengine.memory.vector_memory import VectorMemory
from dreamengine.utils.logger import get_logger

logger = get_logger(__name__)


class DreamAgent:
    """
    A recursive reasoning agent that simulates consciousness-like loops.
    """

    def __init__(self, llm_mode="single", hallucination_level=0.3):
        self.orchestrator = LLMOrchestrator(mode=llm_mode)
        self.memory = VectorMemory()
        self.hallucination_level = hallucination_level
        logger.info(f"DreamAgent initialized in {llm_mode} LLM mode.")

    def think(self, prompt: str, style="factual") -> str:
        """
        One full thought cycle: retrieve → reason → hallucinate → store.
        """
        logger.debug(f"Received prompt: {prompt}")

        # Retrieve past memories
        memories = self.memory.retrieve(prompt)
        context = "\n".join(memories)

        # Construct LLM input
        input_text = f"Context:\n{context}\n\nPrompt:\n{prompt}"

        # Generate response via orchestrator
        response = self.orchestrator.generate(input_text, style=style)

        # Optional hallucination
        if self.hallucination_level > 0:
            response = self._hallucinate(response)

        # Store new memory
        self.memory.store(response)

        return response

    def _hallucinate(self, text: str) -> str:
        # Simulated hallucination (can be replaced with real style transfer later)
        hallucinated = f"{text}\n\n🤖 [hallucinated extension]"
        logger.debug("Hallucination added.")
        return hallucinated

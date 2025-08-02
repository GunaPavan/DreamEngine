from dreamengine.llm.personas import (
    FactualLLM,
    DreamyLLM,
    IntrospectiveLLM
)


class LLMOrchestrator:
    """
    Routes prompts through different cognitive styles,
    using either a shared or separate LLMs per component.
    """

    def __init__(self, mode="single", llm_backend=None):
        self.mode = mode

        if mode == "single":
            self.factual = FactualLLM(shared_llm=llm_backend)
            self.dreamy = DreamyLLM(shared_llm=llm_backend)
            self.introspective = IntrospectiveLLM(shared_llm=llm_backend)
        elif mode == "multi":
            self.factual = FactualLLM()
            self.dreamy = DreamyLLM()
            self.introspective = IntrospectiveLLM()
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def generate(self, prompt: str, style="factual") -> str:
        if style == "factual":
            return self.factual.generate(prompt)
        elif style == "dream":
            return self.dreamy.generate(prompt)
        elif style == "introspective":
            return self.introspective.generate(prompt)
        elif style == "balanced":
            fact = self.factual.generate(prompt)
            dream = self.dreamy.generate(prompt)
            return f"{fact}\n\n[Dream View]\n{dream}"
        else:
            raise ValueError(f"Unknown style: {style}")

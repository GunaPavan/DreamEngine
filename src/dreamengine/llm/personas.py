class FactualLLM:
    def __init__(self, shared_llm=None):
        self.llm = shared_llm or self._default_llm()

    def generate(self, prompt: str) -> str:
        return self.llm.generate(f"[FACTUAL RESPONSE] {prompt}")

    def _default_llm(self):
        from dreamengine.llm.llm_wrapper import LLMWrapper
        return LLMWrapper(model="gpt3")

class DreamyLLM:
    def __init__(self, shared_llm=None):
        self.llm = shared_llm or self._default_llm()

    def generate(self, prompt: str) -> str:
        return self.llm.generate(f"[DREAMY REFLECTION] {prompt}")

    def _default_llm(self):
        from dreamengine.llm.llm_wrapper import LLMWrapper
        return LLMWrapper(model="mixtral")

class IntrospectiveLLM:
    def __init__(self, shared_llm=None):
        self.llm = shared_llm or self._default_llm()

    def generate(self, prompt: str) -> str:
        return self.llm.generate(f"[INTROSPECTIVE THOUGHT] {prompt}")

    def _default_llm(self):
        from dreamengine.llm.llm_wrapper import LLMWrapper
        return LLMWrapper(model="phi3")

# 🧠 DreamEngine

**DreamEngine** is an advanced, cognitively-inspired LLM agent designed to simulate elements of consciousness such as memory drift, hallucinated beliefs, recursive introspection, and dreaming — by leveraging multiple open-source large language models and vector-based memory systems.

> ⚗️ A high-level research + engineering project to push the boundaries of LLM cognition.

---

## 🌌 Project Vision

**What if an LLM could simulate a dream?**
DreamEngine aims to:
- Model cognitive loops using recursive LLM agents
- Emulate hallucinations and belief drift
- Compare behaviors across different open-source LLMs
- Serve as a testbed for cognitive reasoning and introspective thought

This project serves both as a research platform and a high-quality experimental framework for building cognitively aware AI agents.

---

## 💡 Core Features

| Component | Description |
|----------|-------------|
| 🧵 **Recursive DreamAgent** | An agent that thinks in loops, simulates introspection and dreaming |
| 🧠 **LLM Wrapper Layer** | Supports multiple local open-source LLMs, each modular |
| 🪄 **Vector Memory System** | Long-term memory with similarity search, powered by ChromaDB |
| 🌫️ **Hallucination Engine** | Controlled injection of noise or imagined beliefs |
| 🌀 **Context Drift Logic** | Memory reshaping and recursive summarization to simulate belief evolution |
| 🔄 **Multi-Model Experiments** | Test all cognitive components on different LLMs from 1B to 13B+ parameters |

---

## 🧪 Architecture (Modular)

```text
dreamengine/
├── src/
│   └── dreamengine/
│       ├── agents/         # Recursive agents, dreaming logic
│       ├── chains/         # Introspection, summarization, hallucination flows
│       ├── constants/      # Global keys, model configs
│       ├── core/           # DreamKernel and orchestrators
│       ├── evaluation/     # Evaluation logic (not tests)
│       ├── interfaces/     # CLI, Web UI (upcoming)
│       ├── llm/            # Multiple LLM loader modules
│       ├── memory/         # Vector DB interfaces
│       ├── plugins/        # Hallucination, summarizers
│       ├── utils/          # Logging, helpers
│       └── __init__.py
├── tests/
│   ├── test_kernel.py
│   ├── test_memory.py
│   ├── test_introspection.py
│   └── ...
├── .env                   # Environment variables
├── .gitignore
├── LICENSE
├── Makefile
├── pyproject.toml         # Modern dependency + build config
└── README.md              # Project description, architecture, usage, etc.






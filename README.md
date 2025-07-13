# 🧠 DreamEngine

> *Cognitively-inspired AI agent simulating consciousness-like behavior through recursive introspection, hallucinated belief drift, and memory-based dreaming — built with LangChain, local LLMs, and vector memory.*

---

**DreamEngine** is an experimental agent architecture that models emergent cognition in large language models. It emulates how humans dream, misremember, hallucinate beliefs, and reinforce self-narratives. This is achieved through modular recursive loops powered by vector memory (FAISS/Qdrant), local LLMs (Mistral, LLaMA, etc.), and LangChain pipelines.

---

## 🧠 Core Concepts

| Module                  | Simulated Cognitive Function              |
|-------------------------|-------------------------------------------|
| `agent.py`              | Central control loop for recursive thought |
| `memory.py`             | Long-term memory with vector stores        |
| `hallucination.py`      | Belief mutation, synthetic recall          |
| `cognitive_loops.py`    | Dream cycles, introspective reasoning      |
| `examples/simulate_*.py`| Experimental behavior simulation           |

---

## 🚀 Quickstart

```bash
git clone https://github.com/YOUR_USERNAME/DreamEngine.git
cd DreamEngine
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python examples/simulate_dream_cycle.py

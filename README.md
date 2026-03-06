# 🤖 AI Multi-Agent Debate System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%2FGPT--4-green)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful multi-agent debate framework where three AI agents argue both sides of any topic and deliver a structured verdict. Built for reasoning research, policy simulations, and critical thinking exercises.

---

## 🎯 Overview

| Agent | Role | Behavior |
|-------|------|----------|
| 🟢 **Agent A** | Supporter | Argues strongly in favor of the topic |
| 🔴 **Agent B** | Opposer | Argues strongly against the topic |
| ⚖️ **Agent C** | Judge | Evaluates both sides and declares a winner |

---

## 📁 Project Structure

```
ai-multi-agent-debate-system/
├── agents.py            # BaseAgent, SupporterAgent, OpposerAgent, JudgeAgent
├── debate_engine.py     # DebateEngine: orchestrates multi-round debates
├── main.py              # CLI entry point with interactive topic selection
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## ⚡ Quick Start

```bash
# 1. Clone
git clone https://github.com/PranayMahendrakar/ai-multi-agent-debate-system.git
cd ai-multi-agent-debate-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
export OPENAI_API_KEY="your-api-key-here"

# 4. Run!
python main.py --topic "AI will replace human jobs"
```

---

## 💬 Example Output

```
######################################################################
  AI MULTI-AGENT DEBATE SYSTEM
  Topic: AI will replace human jobs
  Rounds: 2 | Model: gpt-3.5-turbo
######################################################################

  ROUND 1 of 2

  Agent A (Supporter)
AI automation is transforming the workforce. Studies show 47% of jobs
face automation risk within 20 years...

  Agent B (Opposer)
History shows technology creates more jobs than it destroys.
The Industrial Revolution created entirely new industries...

  JUDGE'S EVALUATION
WINNER: Agent B (Opposer) — 8.0/10 vs Agent A: 7.5/10
```

---

## 🔧 Python API Usage

```python
from debate_engine import DebateEngine

engine = DebateEngine(
    topic="Universal Basic Income should be implemented globally",
    rounds=2,
    model="gpt-3.5-turbo",
    verbose=True,
    save_transcript=True,
)
results = engine.run()
print(results["verdict"])
```

---

## 🎛️ CLI Options

```
--topic, -t    The debate topic (blank = interactive menu)
--rounds, -r   Number of rounds (default: 2)
--model, -m    OpenAI model (default: gpt-3.5-turbo)
--save, -s     Save transcript to JSON file
--quiet, -q    Only print final verdict
```

---

## 📊 Built-in Example Topics

1. AI will replace most human jobs within 20 years
2. Universal Basic Income should be implemented globally
3. Social media does more harm than good to society
4. Nuclear energy is the best solution to climate change
5. Remote work is more productive than working in an office
6. Cryptocurrencies will replace traditional banking systems
7. Autonomous weapons should be banned internationally
8. Space colonization is essential for humanity survival
9. Mandatory voting should be enforced in democracies
10. Open-source AI models should be freely available to everyone

---

## 🧑‍🔬 Use Cases

- **Reasoning Research** — Study how LLMs argue different positions
- **Policy Simulations** — Explore perspectives on policy topics
- **Critical Thinking** — Generate balanced arguments on any topic
- **Education** — AI-generated debates as teaching material
- **Red-Teaming** — Test LLM reasoning from both sides

---

## ⚙️ Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model` | `gpt-3.5-turbo` | OpenAI model |
| `rounds` | `2` | Number of debate rounds |
| `verbose` | `True` | Print output in real time |
| `save_transcript` | `False` | Save to JSON file |

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

---

## 👨‍💻 Author

**Pranay M Mahendrakar**  
GitHub: [@PranayMahendrakar](https://github.com/PranayMahendrakar)

*Built for AI reasoning research and policy simulations* 🤖

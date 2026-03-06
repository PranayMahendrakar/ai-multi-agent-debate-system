"""
agents.py - AI Multi-Agent Debate System
Defines the three core debate agents: Supporter, Opposer, and Judge.
"""

import openai
from typing import Optional


class BaseAgent:
    """Base class for all debate agents."""

    def __init__(self, name: str, role: str, model: str = "gpt-3.5-turbo"):
        self.name = name
        self.role = role
        self.model = model
        self.history = []

    def _build_system_prompt(self) -> str:
        raise NotImplementedError

    def respond(self, topic: str, context: str = "") -> str:
        system_prompt = self._build_system_prompt()
        messages = [{"role": "system", "content": system_prompt}]
        for entry in self.history:
            messages.append(entry)
        user_content = f"Topic: {topic}"
        if context:
            user_content += f"\n\nPrevious arguments:\n{context}"
        messages.append({"role": "user", "content": user_content})
        response = openai.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.8,
            max_tokens=500,
        )
        reply = response.choices[0].message.content.strip()
        self.history.append({"role": "user", "content": user_content})
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def reset(self):
        self.history = []


class SupporterAgent(BaseAgent):
    def __init__(self, model: str = "gpt-3.5-turbo"):
        super().__init__(name="Agent A (Supporter)", role="supporter", model=model)

    def _build_system_prompt(self) -> str:
        return (
            "You are a skilled debate agent who SUPPORTS the given topic. "
            "Present strong, logical, evidence-based arguments IN FAVOR of the topic. "
            "Be persuasive, structured, and confident. "
            "Keep your argument concise (3-5 key points) and compelling."
        )


class OpposerAgent(BaseAgent):
    def __init__(self, model: str = "gpt-3.5-turbo"):
        super().__init__(name="Agent B (Opposer)", role="opposer", model=model)

    def _build_system_prompt(self) -> str:
        return (
            "You are a skilled debate agent who OPPOSES the given topic. "
            "Present strong, logical, evidence-based arguments AGAINST the topic. "
            "Be persuasive, critical, and incisive. "
            "Keep your argument concise (3-5 key points) and compelling."
        )


class JudgeAgent(BaseAgent):
    def __init__(self, model: str = "gpt-3.5-turbo"):
        super().__init__(name="Agent C (Judge)", role="judge", model=model)

    def _build_system_prompt(self) -> str:
        return (
            "You are an impartial debate judge. Evaluate both sides: assess logical coherence, "
            "evidence quality, persuasiveness, and handling of counterarguments. "
            "Declare a winner with justification and give each side a score out of 10."
        )

    def evaluate(self, topic: str, supporter_arg: str, opposer_arg: str) -> str:
        system_prompt = self._build_system_prompt()
        evaluation_prompt = (
            f"Topic: {topic}\n\n"
            f"--- SUPPORTER'S ARGUMENT ---\n{supporter_arg}\n\n"
            f"--- OPPOSER'S ARGUMENT ---\n{opposer_arg}\n\n"
            "Please provide your evaluation and declare a winner."
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": evaluation_prompt},
        ]
        response = openai.chat.completions.create(
            model=self.model, messages=messages, temperature=0.5, max_tokens=700,
        )
        return response.choices[0].message.content.strip()

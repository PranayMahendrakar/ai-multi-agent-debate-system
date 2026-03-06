"""
debate_engine.py - AI Multi-Agent Debate System
Orchestrates multi-round debates between Supporter, Opposer, and Judge agents.
"""

import os
import json
import time
from datetime import datetime
from typing import Optional

import openai

from agents import SupporterAgent, OpposerAgent, JudgeAgent


class DebateEngine:
    """
    Orchestrates a structured multi-round debate between AI agents.

    Flow:
        Round 1..N:
            - Agent A (Supporter) presents argument
            - Agent B (Opposer) rebuts
        Final:
            - Agent C (Judge) evaluates and declares winner
    """

    def __init__(
        self,
        topic: str,
        rounds: int = 2,
        model: str = "gpt-3.5-turbo",
        verbose: bool = True,
        save_transcript: bool = False,
    ):
        self.topic = topic
        self.rounds = rounds
        self.model = model
        self.verbose = verbose
        self.save_transcript = save_transcript

        self.supporter = SupporterAgent(model=model)
        self.opposer = OpposerAgent(model=model)
        self.judge = JudgeAgent(model=model)

        self.transcript = []

    def _log(self, agent_name: str, text: str):
        """Print and store a transcript entry."""
        separator = "=" * 70
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": agent_name,
            "text": text,
        }
        self.transcript.append(entry)

        if self.verbose:
            print(f"\n{separator}")
            print(f"  {agent_name}")
            print(separator)
            print(text)

    def _build_context(self) -> str:
        """Build a plain-text summary of all previous turns."""
        lines = []
        for entry in self.transcript:
            lines.append(f"[{entry['agent']}]: {entry['text']}")
        return "\n\n".join(lines)

    def run(self) -> dict:
        """Execute the full debate and return the results dict."""
        if self.verbose:
            print("\n" + "#" * 70)
            print(f"  AI MULTI-AGENT DEBATE SYSTEM")
            print(f"  Topic: {self.topic}")
            print(f"  Rounds: {self.rounds} | Model: {self.model}")
            print("#" * 70)

        for round_num in range(1, self.rounds + 1):
            if self.verbose:
                print(f"\n{'=' * 70}")
                print(f"  ROUND {round_num} of {self.rounds}")
                print(f"{'=' * 70}")

            context = self._build_context()

            # Supporter speaks
            supporter_arg = self.supporter.respond(self.topic, context)
            self._log(self.supporter.name, supporter_arg)
            time.sleep(1)

            # Opposer responds
            context = self._build_context()
            opposer_arg = self.opposer.respond(self.topic, context)
            self._log(self.opposer.name, opposer_arg)
            time.sleep(1)

        # Judge evaluates
        if self.verbose:
            print(f"\n{'=' * 70}")
            print("  JUDGE'S EVALUATION")
            print(f"{'=' * 70}")

        supporter_all = "\n\n".join(
            e["text"] for e in self.transcript if "Supporter" in e["agent"]
        )
        opposer_all = "\n\n".join(
            e["text"] for e in self.transcript if "Opposer" in e["agent"]
        )

        verdict = self.judge.evaluate(self.topic, supporter_all, opposer_all)
        self._log(self.judge.name, verdict)

        results = {
            "topic": self.topic,
            "rounds": self.rounds,
            "model": self.model,
            "transcript": self.transcript,
            "verdict": verdict,
        }

        if self.save_transcript:
            self._save(results)

        return results

    def _save(self, results: dict):
        """Save the debate transcript to a JSON file."""
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        safe_topic = "".join(c if c.isalnum() else "_" for c in self.topic)[:40]
        filename = f"debate_{safe_topic}_{ts}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        if self.verbose:
            print(f"\n  Transcript saved to: {filename}")

    def summary(self) -> str:
        """Return a brief text summary of the debate."""
        lines = [f"DEBATE SUMMARY: {self.topic}", "=" * 50]
        for i, entry in enumerate(self.transcript, 1):
            lines.append(f"{i}. [{entry['agent']}]")
            snippet = entry['text'][:200] + "..." if len(entry['text']) > 200 else entry['text']
            lines.append(f"   {snippet}")
            lines.append("")
        return "\n".join(lines)

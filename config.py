"""
config.py - AI Multi-Agent Debate System
Central configuration and constants for the debate system.
"""

import os
from dataclasses import dataclass, field
from typing import List


# ─────────────────────────────────────────────
# OpenAI Configuration
# ─────────────────────────────────────────────

OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", "")
DEFAULT_MODEL: str = "gpt-3.5-turbo"
SUPPORTED_MODELS: List[str] = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-4",
    "gpt-4-turbo",
    "gpt-4o",
]


# ─────────────────────────────────────────────
# Debate Engine Defaults
# ─────────────────────────────────────────────

DEFAULT_ROUNDS: int = 2
MAX_ROUNDS: int = 5
MIN_ROUNDS: int = 1


# ─────────────────────────────────────────────
# Agent Temperature Settings
# ─────────────────────────────────────────────

SUPPORTER_TEMPERATURE: float = 0.8   # Higher = more creative arguments
OPPOSER_TEMPERATURE: float = 0.8     # Higher = more creative arguments
JUDGE_TEMPERATURE: float = 0.5       # Lower = more consistent verdicts


# ─────────────────────────────────────────────
# Token Limits
# ─────────────────────────────────────────────

SUPPORTER_MAX_TOKENS: int = 500
OPPOSER_MAX_TOKENS: int = 500
JUDGE_MAX_TOKENS: int = 700


# ─────────────────────────────────────────────
# Rate Limiting
# ─────────────────────────────────────────────

DELAY_BETWEEN_TURNS: float = 1.0   # Seconds between API calls
DELAY_BETWEEN_ROUNDS: float = 2.0  # Seconds between rounds


# ─────────────────────────────────────────────
# Output Configuration
# ─────────────────────────────────────────────

TRANSCRIPT_DIR: str = "transcripts"
TRANSCRIPT_FORMAT: str = "json"


# ─────────────────────────────────────────────
# Pre-loaded Example Topics
# ─────────────────────────────────────────────

EXAMPLE_TOPICS: List[str] = [
    "Artificial Intelligence will replace most human jobs within 20 years",
    "Universal Basic Income should be implemented globally",
    "Social media does more harm than good to society",
    "Nuclear energy is the best solution to climate change",
    "Remote work is more productive than working in an office",
    "Cryptocurrencies will replace traditional banking systems",
    "Autonomous weapons should be banned internationally",
    "Space colonization is essential for humanity's survival",
    "Mandatory voting should be enforced in democracies",
    "Open-source AI models should be made freely available to everyone",
    "Genetic engineering of humans should be permitted",
    "The death penalty should be abolished worldwide",
    "Privacy is more important than national security",
    "Climate change action should prioritize economy over environment",
    "Animals should have the same rights as humans",
]


# ─────────────────────────────────────────────
# Validation Helper
# ─────────────────────────────────────────────

def validate_config() -> bool:
    """Validate the configuration. Returns True if valid."""
    if not OPENAI_API_KEY:
        print("Warning: OPENAI_API_KEY is not set!")
        return False
    if DEFAULT_MODEL not in SUPPORTED_MODELS:
        print(f"Warning: {DEFAULT_MODEL} is not in supported models list")
        return False
    return True


@dataclass
class DebateConfig:
    """Dataclass for debate configuration with sensible defaults."""
    topic: str
    rounds: int = DEFAULT_ROUNDS
    model: str = DEFAULT_MODEL
    verbose: bool = True
    save_transcript: bool = False
    supporter_temp: float = SUPPORTER_TEMPERATURE
    opposer_temp: float = OPPOSER_TEMPERATURE
    judge_temp: float = JUDGE_TEMPERATURE
    delay_between_turns: float = DELAY_BETWEEN_TURNS

    def __post_init__(self):
        if not self.topic:
            raise ValueError("Topic cannot be empty")
        if not (MIN_ROUNDS <= self.rounds <= MAX_ROUNDS):
            raise ValueError(f"Rounds must be between {MIN_ROUNDS} and {MAX_ROUNDS}")
        if self.model not in SUPPORTED_MODELS:
            print(f"Warning: {self.model} is not in the known supported models list")

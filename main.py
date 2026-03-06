"""
main.py - AI Multi-Agent Debate System
Command-line interface and entry point for the debate system.

Usage:
    python main.py --topic "AI will replace human jobs" --rounds 2
    python main.py --topic "Universal Basic Income" --rounds 3 --save
    python main.py  (interactive mode)
"""

import argparse
import os
import sys

import openai

from debate_engine import DebateEngine


# ─────────────────────────────────────────────
# Pre-loaded example debate topics
# ─────────────────────────────────────────────
EXAMPLE_TOPICS = [
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
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="AI Multi-Agent Debate System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --topic "AI will replace human jobs"
  python main.py --topic "UBI should be universal" --rounds 3 --save
  python main.py --model gpt-4 --topic "Climate change policy"
  python main.py  (launch interactive mode)
        """,
    )
    parser.add_argument(
        "--topic", "-t",
        type=str,
        default=None,
        help="The debate topic (or leave blank for interactive selection)",
    )
    parser.add_argument(
        "--rounds", "-r",
        type=int,
        default=2,
        help="Number of debate rounds (default: 2)",
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="gpt-3.5-turbo",
        help="OpenAI model to use (default: gpt-3.5-turbo)",
    )
    parser.add_argument(
        "--save", "-s",
        action="store_true",
        help="Save the full transcript to a JSON file",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress verbose output (only print final verdict)",
    )
    return parser.parse_args()


def select_topic_interactive() -> str:
    """Let the user pick a topic interactively."""
    print("\n" + "=" * 60)
    print("  AI MULTI-AGENT DEBATE SYSTEM — Topic Selection")
    print("=" * 60)
    print("\nChoose a debate topic:\n")
    for i, topic in enumerate(EXAMPLE_TOPICS, 1):
        print(f"  {i:>2}. {topic}")
    print(f"  {'C':>2}. Enter a custom topic")
    print()

    while True:
        choice = input("Enter number or 'C' for custom: ").strip()
        if choice.upper() == "C":
            topic = input("Enter your custom topic: ").strip()
            if topic:
                return topic
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(EXAMPLE_TOPICS):
                return EXAMPLE_TOPICS[idx]
        print("  Invalid choice. Please try again.")


def setup_openai_key():
    """Ensure the OpenAI API key is available."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("\nError: OPENAI_API_KEY environment variable is not set.")
        print("Please set it with:")
        print("  export OPENAI_API_KEY='your-api-key-here'  (Linux/macOS)")
        print("  set OPENAI_API_KEY=your-api-key-here        (Windows)")
        sys.exit(1)
    openai.api_key = api_key


def main():
    args = parse_args()
    setup_openai_key()

    # Determine topic
    topic = args.topic
    if not topic:
        topic = select_topic_interactive()

    # Run the debate
    engine = DebateEngine(
        topic=topic,
        rounds=args.rounds,
        model=args.model,
        verbose=not args.quiet,
        save_transcript=args.save,
    )

    results = engine.run()

    # If quiet mode, print just the verdict
    if args.quiet:
        print("\n" + "=" * 70)
        print("DEBATE VERDICT")
        print("=" * 70)
        print(results["verdict"])

    print("\n" + "=" * 70)
    print("Debate complete!")
    print("=" * 70)

    return results


if __name__ == "__main__":
    main()

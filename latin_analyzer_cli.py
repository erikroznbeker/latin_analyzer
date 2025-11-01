#!/usr/bin/env python3
"""
Interactive CLI for Latin Language Analyzer
Allows users to input custom Latin text for analysis.
"""

import sys
from latin_analyzer import LatinAnalyzer


def print_banner():
    """Print application banner."""
    print("\n" + "="*70)
    print(" " * 15 + "LATIN LANGUAGE ANALYZER")
    print("="*70)
    print("Analizira latinski tekst i pruža morfološku analizu svake riječi.")
    print("="*70 + "\n")


def print_help():
    """Print usage help."""
    print("\nUpute:")
    print("  - Unesi latinski tekst (možeš koristiti više linija)")
    print("  - Upiši 'done' ili pritisni prazan Enter za analizu")
    print("  - Upiši 'q' ili 'quit' za izlaz")
    print("  - Upiši 'help' za ove upute")
    print()


def get_multiline_input():
    """Get multiline input from user."""
    print("Unesi latinski tekst. Kad završiš, upiši 'done' ili pritisni Enter na praznoj liniji.")
    print("-" * 70)

    lines = []

    while True:
        try:
            line = input("> " if not lines else "  ")

            # Check for quit commands
            if line.strip().lower() in ['q', 'quit', 'exit']:
                return None

            # Check for done command
            if line.strip().lower() == 'done':
                if lines:
                    break
                else:
                    print("(Unesi neki tekst prvo)")
                    continue

            # Check for help
            if line.strip().lower() == 'help':
                print_help()
                continue

            # Empty line - if we have text, analyze; otherwise continue
            if not line.strip():
                if lines:
                    # We have text, proceed to analysis
                    break
                else:
                    # No text yet, just continue
                    continue

            # Non-empty line - add to our text
            lines.append(line)

        except EOFError:
            break

    return '\n'.join(lines).strip()


def main():
    """Main CLI function."""

    print_banner()

    # Initialize analyzer
    print("Inicijalizacija CLTK modela...")
    print("(Prvo pokretanje može potrajati jer se preuzimaju modeli)\n")

    try:
        analyzer = LatinAnalyzer()
    except Exception as e:
        print(f"\n✗ Greška pri inicijalizaciji: {e}")
        print("\nMolimo pokreni 'download_models.sh' za preuzimanje potrebnih modela.")
        sys.exit(1)

    print("\n✓ Analyzer je spreman!\n")
    print_help()

    # Main loop
    while True:
        # Get input
        text = get_multiline_input()

        # Check if user wants to quit
        if text is None:
            print("\nHvala što si koristio Latin Analyzer. Doviđenja!")
            break

        # Check if empty
        if not text:
            print("⚠ Tekst je prazan. Molimo unesi neki latinski tekst.\n")
            continue

        # Analyze text
        print("\n" + "="*70)
        print("ANALIZA:")
        print("="*70)

        try:
            result = analyzer.analyze_and_format(text)
            print(result)
        except Exception as e:
            print(f"\n✗ Greška pri analizi: {e}")
            print("Molimo provjeri da li je tekst ispravan latinski tekst.")

        print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrekinuto. Doviđenja!")
        sys.exit(0)

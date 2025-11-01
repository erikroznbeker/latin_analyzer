"""
Setup script to download required CLTK and Stanza models for Latin.
Run this before using the Latin analyzer.
"""

import os
from cltk.data.fetch import FetchCorpus

def setup_models():
    """Download required models for Latin analysis."""

    print("Setting up Latin language models for CLTK...")
    print("This will download approximately 200MB of data.")
    print()

    # Download Latin models
    try:
        # Fetch Latin models
        corpus_downloader = FetchCorpus(language="lat")

        # Download available corpora
        print("Downloading Latin models...")

        # Note: CLTK will automatically download Stanza models when needed
        # We just need to trigger it programmatically

        print("\nNow initializing NLP pipeline to download Stanza models...")
        print("Please answer 'Y' when prompted to download models.")

        from cltk import NLP
        nlp = NLP(language="lat", suppress_banner=True)

        # Test with a simple sentence
        test_doc = nlp.analyze("Gallia est omnis divisa in partes tres.")

        print("\n✓ Setup completed successfully!")
        print(f"✓ Analyzed {len(test_doc.words)} words in test sentence.")
        print("\nYou can now use latin_analyzer.py")

    except Exception as e:
        print(f"\n✗ Error during setup: {e}")
        print("\nPlease try running setup again or install models manually.")
        print("See: https://docs.cltk.org/ for more information.")


if __name__ == "__main__":
    setup_models()

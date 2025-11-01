"""
Setup script to download required CLTK and Stanza models for Latin.
Run this before using the Latin analyzer.

CLTK 2.x compatible version - uses same initialization as latin_analyzer.py
"""

def setup_models():
    """Download required models for Latin analysis."""

    print("Setting up Latin language models for CLTK 2.x...")
    print("This will download approximately 250MB of data.")
    print()

    try:
        print("Initializing CLTK 2.x NLP pipeline for Latin...")
        print("Models will be downloaded automatically on first use.")
        print()

        # Import CLTK 2.x NLP (same as latin_analyzer.py)
        from cltk.nlp import NLP

        # Initialize NLP - this will trigger model downloads
        # User will be prompted to confirm download
        print("Note: You will be asked to confirm the download (type 'Y' or press Enter).")
        print()

        # Initialize with CLTK 2.x API using Stanza backend
        nlp = NLP("lati1261", backend="stanza", suppress_banner=True)

        # Test with a simple sentence to ensure everything works
        print("Testing analysis with sample sentence...")
        test_doc = nlp.analyze("Gallia est omnis divisa in partes tres.")

        print("\n" + "="*60)
        print("✓ Setup completed successfully!")
        print(f"✓ Analyzed {len(test_doc.words)} words in test sentence.")
        print("="*60)
        print("\nYou can now use:")
        print("  - python latin_analyzer.py (demo)")
        print("  - python latin_analyzer_cli.py (interactive)")
        print()

    except KeyboardInterrupt:
        print("\n\n✗ Setup cancelled by user.")
        print("Run this script again when ready to download models.")

    except Exception as e:
        print(f"\n✗ Error during setup: {e}")
        print("\nTroubleshooting:")
        print("  1. Ensure you have a stable internet connection")
        print("  2. Check that you have ~250MB of free disk space")
        print("  3. Try running: pip install --upgrade cltk")
        print("  4. See: https://docs.cltk.org/ for more information")
        print()


if __name__ == "__main__":
    setup_models()

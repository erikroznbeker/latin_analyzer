#!/bin/bash
# Script to automatically download CLTK 2.x Stanza models for Latin

echo "Downloading Latin models for CLTK 2.x..."
echo "This will automatically accept the download prompt."
echo ""

# Automatically answer 'Y' to the Stanza download prompt
echo "Y" | python3 -c "
from cltk.nlp import NLP
nlp = NLP('lati1261', backend='stanza', suppress_banner=True)
doc = nlp.analyze('Gallia est omnis divisa in partes tres.')
print('\n✓ Models downloaded successfully!')
print(f'✓ Test analysis completed: {len(doc.words)} words processed.')
"

echo ""
echo "Setup complete! You can now use latin_analyzer.py"

#!/bin/bash
# Script to automatically download CLTK Stanza models for Latin

echo "Downloading Latin models for CLTK..."
echo "This will automatically accept the download prompt."
echo ""

# Automatically answer 'Y' to the Stanza download prompt
echo "Y" | python3 -c "
from cltk import NLP
nlp = NLP(language='lat', suppress_banner=True)
doc = nlp.analyze('Gallia est omnis divisa in partes tres.')
print('\n✓ Models downloaded successfully!')
print(f'✓ Test analysis completed: {len(doc.words)} words processed.')
"

echo ""
echo "Setup complete! You can now use latin_analyzer.py"

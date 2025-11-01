"""
Latin Language Analyzer using CLTK 2.x
Analyzes Latin text and provides morphological analysis, lemmatization, and POS tagging.
"""

from cltk.nlp import NLP
from cltk.core.data_types import Doc, Word
from typing import List, Dict


class LatinAnalyzer:
    """Analyzer for Latin text using CLTK."""

    # Mapping of Universal Dependencies POS tags to Croatian/English descriptions
    POS_MAP = {
        'NOUN': 'imenica / noun',
        'VERB': 'glagol / verb',
        'ADJ': 'pridjev / adjective',
        'ADV': 'prilog / adverb',
        'PRON': 'zamjenica / pronoun',
        'ADP': 'prijedlog / preposition',
        'CONJ': 'veznik / conjunction',
        'CCONJ': 'sastavni veznik / coordinating conjunction',
        'SCONJ': 'podredni veznik / subordinating conjunction',
        'DET': 'član / determiner',
        'NUM': 'broj / numeral',
        'PART': 'čestica / particle',
        'INTJ': 'uzvik / interjection',
        'PUNCT': 'interpunkcija / punctuation',
        'X': 'ostalo / other'
    }

    # Mapping for morphological features
    CASE_MAP = {
        'Nom': 'N (nominativ)',
        'Gen': 'G (genitiv)',
        'Dat': 'D (dativ)',
        'Acc': 'A (akuzativ)',
        'Abl': 'Ab (ablativ)',
        'Voc': 'V (vokativ)',
        'Loc': 'L (lokativ)',
        # Also handle full names from CLTK features
        'nominative': 'N (nominativ)',
        'genitive': 'G (genitiv)',
        'dative': 'D (dativ)',
        'accusative': 'A (akuzativ)',
        'ablative': 'Ab (ablativ)',
        'vocative': 'V (vokativ)',
        'locative': 'L (lokativ)'
    }

    NUMBER_MAP = {
        'Sing': 'sg (jednina)',
        'Plur': 'pl (množina)',
        # Also handle full names from CLTK features
        'singular': 'sg (jednina)',
        'plural': 'pl (množina)'
    }

    GENDER_MAP = {
        'Masc': 'm (muški rod)',
        'Fem': 'f (ženski rod)',
        'Neut': 'n (srednji rod)',
        # Also handle full names from CLTK features
        'masculine': 'm (muški rod)',
        'feminine': 'f (ženski rod)',
        'neuter': 'n (srednji rod)'
    }

    TENSE_MAP = {
        'Pres': 'prezent',
        'Perf': 'perfekt',
        'Fut': 'futur',
        'Past': 'prošlo vrijeme',
        'Imp': 'imperfekt',
        'Pqp': 'pluskvamperfekt',
        # Also handle full names from CLTK features
        'present': 'prezent',
        'perfect': 'perfekt',
        'future': 'futur',
        'past': 'prošlo vrijeme',
        'imperfect': 'imperfekt',
        'pluperfect': 'pluskvamperfekt'
    }

    MOOD_MAP = {
        'Ind': 'indikativ',
        'Imp': 'imperativ',
        'Sub': 'konjunktiv',
        'Inf': 'infinitiv',
        'Part': 'particip',
        # Also handle full names from CLTK features
        'indicative': 'indikativ',
        'imperative': 'imperativ',
        'subjunctive': 'konjunktiv',
        'infinitive': 'infinitiv',
        'participle': 'particip'
    }

    VOICE_MAP = {
        'Act': 'aktiv',
        'Pass': 'pasiv',
        # Also handle full names from CLTK features
        'active': 'aktiv',
        'passive': 'pasiv'
    }

    PERSON_MAP = {
        '1': '1. l.',
        '2': '2. l.',
        '3': '3. l.'
    }

    def __init__(self):
        """Initialize the Latin NLP pipeline using CLTK 2.x with Stanza backend."""
        print("Initializing CLTK 2.x Latin NLP pipeline...")
        print("Note: First run will download required models (~200MB)")

        # Initialize NLP with Stanza backend (CLTK 2.x API)
        # "lati1261" is the Glottolog code for Latin
        self.nlp = NLP("lati1261", backend="stanza", suppress_banner=True)
        print("CLTK 2.x initialized successfully!")

    def analyze_text(self, text: str) -> Doc:
        """
        Analyze Latin text using CLTK pipeline.

        Args:
            text: Latin text to analyze

        Returns:
            CLTK Doc object with analyzed text
        """
        return self.nlp.analyze(text=text)

    def format_morphology(self, word: Word) -> str:
        """
        Format morphological features of a word (CLTK 2.x).

        Args:
            word: CLTK Word object

        Returns:
            Formatted morphological description
        """
        features = []

        # Skip punctuation
        if hasattr(word.upos, 'tag') and word.upos.tag == 'PUNCT':
            return ''

        # Access features from CLTK 2.x UDFeatureTagSet
        if not word.features:
            return ''

        # Convert UDFeatureTagSet to dictionary
        # word.features is iterable and returns ('features', [UDFeatureTag, ...])
        morph = {}
        for feature_set in word.features:
            if isinstance(feature_set, tuple):
                _, tag_list = feature_set
                for tag in tag_list:
                    # Each tag has .key and .value attributes
                    tag_dict = tag.model_dump()
                    morph[tag_dict['key']] = tag_dict['value']

        # Case
        if 'Case' in morph:
            features.append(self.CASE_MAP.get(morph['Case'], morph['Case']))

        # Number
        if 'Number' in morph:
            features.append(self.NUMBER_MAP.get(morph['Number'], morph['Number']))

        # Gender
        if 'Gender' in morph:
            features.append(self.GENDER_MAP.get(morph['Gender'], morph['Gender']))

        # For verbs
        upos_tag = word.upos.tag if hasattr(word.upos, 'tag') else str(word.upos)
        if upos_tag == 'VERB':
            # Person
            if 'Person' in morph:
                features.append(self.PERSON_MAP.get(morph['Person'], morph['Person']))

            # Tense
            if 'Tense' in morph:
                features.append(self.TENSE_MAP.get(morph['Tense'], morph['Tense']))

            # Mood
            if 'Mood' in morph:
                features.append(self.MOOD_MAP.get(morph['Mood'], morph['Mood']))

            # Voice
            if 'Voice' in morph:
                features.append(self.VOICE_MAP.get(morph['Voice'], morph['Voice']))

        return ' '.join(features) if features else ''

    def analyze_and_format(self, text: str) -> str:
        """
        Analyze Latin text and format output in the desired format.

        Args:
            text: Latin text to analyze

        Returns:
            Formatted analysis string
        """
        doc = self.analyze_text(text)

        results = []

        for word in doc.words:
            # Get UPOS tag (handle CLTK 2.x enum)
            upos_tag = word.upos.tag if hasattr(word.upos, 'tag') else str(word.upos)

            # Skip punctuation
            if upos_tag == 'PUNCT':
                continue

            # Get word form
            word_form = word.string

            # Get lemma (dictionary form)
            lemma = word.lemma if word.lemma else word.string

            # Get morphological features
            morph_desc = self.format_morphology(word)

            # Get POS description
            pos_desc = self.POS_MAP.get(upos_tag, upos_tag)

            # Format: word – morphology od lemma = (translation would go here)
            if morph_desc:
                line = f"{word_form} – {morph_desc} od {lemma} ({pos_desc})"
            else:
                line = f"{word_form} – {lemma} ({pos_desc})"

            results.append(line)

        return '\n'.join(results)


def main():
    """Main function to demonstrate the analyzer."""

    # Example text from Horace, Odes 3.30
    text = """Exegi monumentum aere perennius
    regalique situ pyramidum altius,
    quod non imber edax, non aquilo impotens
    possit diruere aut innumerabilis
    annorum series et fuga temporum."""

    # Initialize analyzer
    analyzer = LatinAnalyzer()

    # Analyze and print results
    print("\n" + "="*60)
    print("LATIN TEXT ANALYSIS")
    print("="*60)
    print(f"\nOriginal text:\n{text}\n")
    print("="*60)
    print("ANALYSIS:")
    print("="*60)

    result = analyzer.analyze_and_format(text)
    print(result)
    print("\n" + "="*60)


if __name__ == "__main__":
    main()

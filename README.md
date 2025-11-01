# Latin Language Analyzer

Aplikacija za morfološku analizu latinskog teksta pomoću CLTK (Classical Language Toolkit).

## Mogućnosti

Za svaku riječ u latinskom tekstu, aplikacija pruža:
- **Lemmatizaciju** - osnovni oblik riječi (dictionary form)
- **Morfološku analizu** - padež, broj, rod, vrijeme, način, osoba itd.
- **POS tagging** - vrsta riječi (imenica, glagol, pridjev...)

## Primjer

### Ulaz:
```
Exegi monumentum aere perennius
regalique situ pyramidum altius...
```

### Izlaz:
```
Exegi – sg (jednina) 2. l. prezent indikativ aktiv od exego (glagol / verb)
monumentum – A (akuzativ) sg (jednina) n (srednji rod) od monumentum (imenica / noun)
aere – Ab (ablativ) sg (jednina) m (muški rod) od aer (imenica / noun)
perennius – A (akuzativ) sg (jednina) n (srednji rod) aktiv od perennio (glagol / verb)
...
```

## Instalacija

### Zahtjevi

- **Python 3.8 - 3.12** (preporučeno 3.10 ili 3.11)
- **CLTK 1.x** (aplikacija je pisana za CLTK 1.5.0)

**Napomena:** CLTK 2.x ima breaking changes. Ova aplikacija trenutno podržava CLTK 1.x.

### 1. Instaliraj Python dependencies

```bash
pip install cltk[stanza]
```

**Napomena:** Važno je instalirati `cltk[stanza]` (sa Stanza ekstenzijom) jer aplikacija koristi Stanza backend za morfološku analizu.

### 2. Preuzmi potrebne modele

Pokreni setup skriptu koja će automatski preuzeti Stanza i CLTK modele (~250MB):

```bash
chmod +x download_models.sh
./download_models.sh
```

Alternativno, možeš ručno preuzeti modele:

```bash
python3 setup_models.py
```

### Windows korisnici

**Automatska instalacija (preporučeno):**

Jednostavno pokreni batch skriptu koja će instalirati sve automatski:

```bash
install_windows.bat
```

Ova skripta će:
1. Provjeriti da li je Python instaliran
2. Instalirati dependencies (cltk)
3. Preuzeti potrebne modele (~250MB)

**Ručna instalacija:**

Alternativno, možeš ručno instalirati:

```bash
# Instalacija dependencies (sa Stanza ekstenzijom)
pip install cltk[stanza]

# Preuzimanje modela
python setup_models.py
```

**Napomena:** Na Windows-u koristi `python` umjesto `python3` u svim komandama:
```bash
# Primjeri:
python setup_models.py
python latin_analyzer_cli.py
python latin_analyzer.py
```

## Korištenje

### 1. Interaktivni CLI (preporučeno)

```bash
python3 latin_analyzer_cli.py
```

Ovo pokreće interaktivno sučelje gdje možeš:
- Unositi vlastiti latinski tekst
- Koristiti više linija teksta
- Analizirati više puta bez ponovnog pokretanja

### 2. Demo primjer

```bash
python3 latin_analyzer.py
```

Ovo će analizirati demo tekst iz Horacija (Ode 3.30).

### 3. Korištenje u Python skripti

```python
from latin_analyzer import LatinAnalyzer

# Inicijalizacija
analyzer = LatinAnalyzer()

# Analiziraj tekst
text = "Gallia est omnis divisa in partes tres."
result = analyzer.analyze_and_format(text)

print(result)
```

### 4. Jedan red (single command)

```bash
echo "Gallia est omnis divisa in partes tres." | python3 -c "
from latin_analyzer import LatinAnalyzer
import sys
analyzer = LatinAnalyzer()
text = sys.stdin.read()
print(analyzer.analyze_and_format(text))
"
```

## Struktura projekta

```
latin/
├── latin_analyzer.py       # Glavna biblioteka za analizu
├── latin_analyzer_cli.py   # Interaktivni CLI
├── setup_models.py         # Setup skripta za modele
├── download_models.sh      # Bash skripta za automatsko preuzimanje
├── requirements.txt        # Python dependencies
└── README.md              # Ova datoteka
```

## Objašnjenje skraćenica

### Padeži:
- **N** - Nominativ
- **G** - Genitiv
- **D** - Dativ
- **A** - Akuzativ
- **Ab** - Ablativ
- **V** - Vokativ
- **L** - Lokativ

### Broj:
- **sg** - Jednina (singular)
- **pl** - Množina (plural)

### Rod:
- **m** - Muški rod (masculine)
- **f** - Ženski rod (feminine)
- **n** - Srednji rod (neuter)

### Glagolski oblici:
- **1. l. / 2. l. / 3. l.** - Prvo, drugo, treće lice
- **prezent** - Prezent
- **perfekt** - Perfekt
- **imperfekt** - Imperfekt
- **futur** - Futur
- **pluskvamperfekt** - Pluskvamperfekt
- **indikativ** - Indikativ
- **konjunktiv** - Konjunktiv
- **imperativ** - Imperativ
- **infinitiv** - Infinitiv
- **particip** - Particip
- **aktiv** - Aktivni glas
- **pasiv** - Pasivni glas

## Tehnologije

- **CLTK** - Classical Language Toolkit za NLP procesiranje klasičnih jezika
- **Stanza** - Stanford NLP biblioteka za morfološku analizu
- **Python 3.8+**

## Napomene

- Prvi put kada pokreneš aplikaciju, CLTK će automatski preuzeti potrebne modele (oko 250MB)
- Lemmatizacija i morfološka analiza imaju točnost preko 90%
- CLTK koristi Universal Dependencies standard za morfološke značajke
- Aplikacija trenutno ne pruža prijevode riječi, samo morfološku analizu

## Potencijalna poboljšanja

- [ ] Dodavanje prijevoda riječi (integracija s latinskim rječnikom)
- [ ] Web sučelje
- [ ] Export u različite formate (JSON, CSV, XML)
- [ ] Podrška za analizu cijelih dokumenata
- [ ] Sintaktička analiza (dependency parsing)
- [ ] Vizualizacija sintaktičkog stabla

## Licenca

Open source - koristi slobodno za obrazovne ili istraživačke svrhe.

## Reference

- CLTK Documentation: https://docs.cltk.org/
- Stanza: https://stanfordnlp.github.io/stanza/
- Universal Dependencies: https://universaldependencies.org/

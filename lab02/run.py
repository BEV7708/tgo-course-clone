"""Лабораторная 2. Задание: assignments/02/README.md в репозитории курса.

Запуск: python lab02/run.py, для CI python lab02/run.py --fast.
"""
import argparse
import re
import json
import urllib.request

from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTIFACTS = HERE / "artifacts"
CORPUS_URL = (
    "https://raw.githubusercontent.com/nevmenandr/"
    "word2vec-russian-novels/master/books_before/WarAndPeace.txt"
)
CORPUS_PATH = HERE.parent / "demos" / "02"

def ensure_corpus() -> Path:
    if not CORPUS_PATH.exists():
        print(f"[corpus] скачиваю {CORPUS_URL}")
        urllib.request.urlretrieve(CORPUS_URL, CORPUS_PATH)
    else:
        print(f"[corpus] использую локальный {CORPUS_PATH}")
    return CORPUS_PATH
    
def read_corpus(fast: bool) -> str:
    text = CORPUS_PATH.read_text(encoding="utf-8")
    return text

def normalize(text: str) -> str:
    return text.lower().replace("ё", "е")

def extract_word_counts(text: str, min_freq: int) -> Counter:
    counts = Counter(re.compile(r"[а-я]+(?:-[а-я]+)*").findall(text))
    return Counter({w: c for w, c in counts.items() if c >= min_freq})

def word_to_symbols(word: str) -> tuple:
    return tuple(word) + ("</w>",)
    
def get_pair_stats(vocab: Counter) -> Counter:
    pairs = Counter()
    for symbols, freq in vocab.items():
        for a, b in zip(symbols, symbols[1:]):
            pairs[(a, b)] += freq
    return pairs
    
def merge_pair(pair: tuple, vocab: Counter) -> Counter:
    a, b = pair
    merged = a + b
    new_vocab = Counter()
    for symbols, freq in vocab.items():
        out, i = [], 0
        while i < len(symbols):
            if i < len(symbols) - 1 and symbols[i] == a and symbols[i + 1] == b:
                out.append(merged)
                i += 2
            else:
                out.append(symbols[i])
                i += 1
        new_vocab[tuple(out)] = freq
    return new_vocab

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="быстрый режим для CI")
    args = ap.parse_args()
    ARTIFACTS.mkdir(exist_ok=True)

if __name__ == "__main__":
    main()
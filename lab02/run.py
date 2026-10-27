"""Лабораторная 2. Задание: assignments/02/README.md в репозитории курса.

Запуск: python lab02/run.py, для CI python lab02/run.py --fast.
"""
import argparse
import re
import json

from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTIFACTS = HERE / "artifacts"
CORPUS_PATH = HERE.parent / "demos" / "02"

def normalize(text: str) -> str:
    return text.lower().replace("ё", "е")

def extract_word_counts(text: str, min_freq: int) -> Counter:
    counts = Counter(WORD_RE.findall(text))
    return Counter({w: c for w, c in counts.items() if c >= min_freq})

def word_to_symbols(word: str) -> tuple:
    return tuple(word) + (END,)
    
    



def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="быстрый режим для CI")
    args = ap.parse_args()
    ARTIFACTS.mkdir(exist_ok=True)
    raise NotImplementedError("работа не начата")


if __name__ == "__main__":
    main()

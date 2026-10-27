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

def word_to_symbols(word: str) -> tuple:
    return tuple(word) + ("</w>",)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="быстрый режим для CI")
    args = ap.parse_args()
    ARTIFACTS.mkdir(exist_ok=True)

if __name__ == "__main__":
    main()
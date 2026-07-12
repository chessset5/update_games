"""
gets potential name from folder
"""

from pathlib import Path

import re


def tokenizer(text: str) -> list[str]:
    # 1. Match a sequence of numbers: \d+
    # 2. Match a title name or capitalized word: [A-Z][a-z]*
    # 3. Match a sequence of lowercase letters: [a-z]+
    # 4. Match any remaining uppercase blocks: [A-Z]+
    pattern = r"\d+|[A-Z][a-z]*|[a-z]+|[A-Z]+"

    return re.findall(pattern, text)


def score(name: str, tokens: list[str]) -> int:
    sv = 0
    for t in tokens:
        if t in name:
            sv += 1
    return sv


def __debug_get_exe(exes: list[Path], tokens) -> list:
    data: list = []
    for i in exes:
        data.append(f"{score(i.name, tokens)} | {i.name}")
    return data


def get_exes(folder: Path) -> list[Path]:
    folder_name: str = folder.name
    name_components: list[str] = tokenizer(folder_name)

    exes: list[Path] = list()

    for r, ds, fs in folder.walk():
        for f in fs:
            p: Path = r / f
            if p.suffix == ".exe":
                if score(p.stem, name_components) > 0:
                    exes.append(p)

    return exes

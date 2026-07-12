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
    token_len: int = len(name_components)

    # adding for exe like AC.exe for "assassins's creed"
    nc_s: set[str] | list[str] = set(name_components)
    for nc in name_components:
        if nc[0].isalpha() and nc[0].isupper():
            nc_s.add(nc[0])

    exes: list[Path] = list()

    nc_l = list(nc_s)

    for r, ds, fs in folder.walk():
        for f in fs:
            p: Path = r / f
            if p.suffix == ".exe":
                if score(p.stem, nc_l) >= token_len:
                    exes.append(p)


    return exes

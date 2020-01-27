import os
from typing import List, Optional


def group_content(files: List[str]) -> List[Optional[str]]:
    content = []
    for file in files:
        f = open(file, "r", encoding="utf-8")
        content += f.read().splitlines()
        f.close()

    return content


def remove(files: List[str]) -> None:
    for file in files:
        os.remove(file)

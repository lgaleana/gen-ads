import os
from typing import Any, Dict, List

import openai

openai.api_key = os.environ["OPENAI_KEY_PERSONAL"]


def gen(prompt: str, n: int, size: str) -> Dict[str, Any]:
    return openai.Image.create(prompt=prompt, n=n, size=size)  # type: ignore


def urls(prompt: str, n: int = 4, size: str = "512x512") -> List[str]:
    images = gen(prompt, n, size)
    return [i["url"] for i in images["data"]]  # type: ignore
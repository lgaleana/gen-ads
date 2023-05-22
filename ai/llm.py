import os
from typing import Any, Dict, List, Optional

import openai


openai.api_key = os.environ["OPENAI_KEY_PERSONAL"]
MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.6


def call(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    stop: Optional[str] = None,
) -> Dict[str, Any]:
    if not model:
        model = MODEL
    if not temperature:
        temperature = TEMPERATURE

    return openai.ChatCompletion.create(  # type: ignore
        model=model,
        messages=messages,
        temperature=temperature,
        stop=stop,
    )


def next(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    stop: Optional[str] = None,
) -> str:
    return call(messages, model, temperature, stop)["choices"][0]["message"]["content"]

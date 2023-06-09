from typing import Dict

from ai import image
from ai_tasks.headlines_for_images import get_headlines_for_images
from ai_tasks.headlines_ai_images import generate_headlines
from ai_tasks.text_summary import summarize_text
from code_tasks.custom import get_image_info, run_parallel_jobs
from code_tasks.images_in_url import get_images_from_url
from code_tasks.text_in_url import get_text_from_url
from utils.io import print_assistant, print_system, user_input


DIMENSIONS = [
    "300x50",
    "300x250",
    "300x600",
    "728x90",
    "160x600",
]


def run():
    url = user_input("URL: ")

    # Code tasks (most code was generated by ChatGPT-4)
    print_system("Getting URL data...")
    text = get_text_from_url(url)
    images = get_images_from_url(url)
    image_info = run_parallel_jobs(get_image_info, images, max=10)

    # AI tasks
    summary = summarize_text(text)
    print_assistant(summary)
    headlines = get_headlines_for_images(summary, DIMENSIONS, image_info)
    print_assistant(headlines)

    headlines_prompts = generate_headlines(summary, DIMENSIONS)
    print_system("Generating AI images...")
    run_parallel_jobs(gen_image, headlines_prompts)


def gen_image(input: Dict[str, str]) -> None:
    ai_image = image.urls(input["prompt"], size=input["dimension_to_map"])[0]
    print_system(f"Prompt: {input['prompt']}")
    print_assistant(input["ad_dimension"])
    print_assistant(input["headline"])
    print_assistant(ai_image)

import re


def clear_tags(text: str) -> str:
    return re.sub("<.*?>|\xa0|\n|\t", "", text)
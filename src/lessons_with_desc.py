from config import clear_tags
import re


lesson_pattern = r"<strong>.*?<\/strong>|<li>.*?<\/li>"
split_pattern = r"<strong>.*?<\/strong>"
desc_pattern = r"<p>.*?<\/p>"


def build_lesson_with_desc_type(program: str) -> str:
    result: list[dict] = []
    lessons = re.findall(lesson_pattern, program)
    lessons_desc = re.split(split_pattern, program)
    
    for i, lesson in enumerate(lessons):
        try:desc = re.findall(desc_pattern, lessons_desc[i+1])[0]
        except IndexError:desc = ""

        result.append({
            "name": clear_tags(lesson),
            "desc": clear_tags(desc)
        })
    return [{
        "name": "",
        "lessons": result
    }]

from config import *
import re

strong_pattern = r"<strong>Раздел.*?<\/strong>.*?\n|<strong>РАЗДЕЛ.*?<\/strong>.*?\n|<strong>Тема.*?<\/strong>.*?\n|<strong>Модуль.*?<\/strong>.*?\n"
p_pattern = r"<p>Тема.*?<\/p>.*?\n|<p><em>Тема.*?<\/p>|<p>Раздел.*?<\/p>|Тема.*?<br>|<p>Модуль.*?<\/p>|Модуль.*?<br>|Модуль.*?<\/p>|<p>РАЗДЕЛ.*?<\/p>|Раздел \d+.*?<br>"
li_pattern = r"<li>Модуль.*?<\/li>|<li>Тема .*?<\/li>"
td_pattern = r"<td>Тема.*?</td>|<td>Модуль.*?<\/td>"
roman_symbols_pattern = r"Раздел.*?[A-Z]{1,4}.*?<\/p>|Раздел.*?[A-Z]{1,4}.*?<br>"
module_pattern = f"{strong_pattern}|{p_pattern}|{roman_symbols_pattern}|{li_pattern}|{td_pattern}"


def build_module_type(program: str) -> str:
    """Как должна выглядеть программа с модулями:
        [
            {
                "name": "Модуль 1 (или его название) ",
                "lessons": [
                    {
                        "name": "Урок 1 (или его название)",
                        "desc": "Описание урока 1",
                    },
                    .....
                    {
                        "name": "Урок n (или его название)",
                        "desc": "Описание урока n",
                    },
                ]
            },
            ......
            {
                "name": "Модуль n (или его название) ",
                "lessons": [
                    {
                        "name": "Урок 1 (или его название)",
                        "desc": "Описание урока 1",
                    },
                    {
                        "name": "Урок n (или его название)",
                        "desc": "Описание урока n",
                    },
                ]
            },
        ]

    """
    
    result: list[dict] = []
    modules =  re.findall(module_pattern, program)
    module_lessons = re.split(module_pattern, program)
    for i, module in enumerate(modules):
        result.append({
            "name": clear_tags(module),
            "lessons": []
        })
        if not module_lessons: continue
        lessons = re.finditer(r".*?<br>|^(?!.*(<strong>)).*?<\/p>|<li>.*?<\/li>", module_lessons[i+1], re.MULTILINE)
        for lesson in lessons:
            result[i]["lessons"].append({
                "name": clear_tags(lesson.group()),
                "desc": ""
            })
    return result 
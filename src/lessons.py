import re
from config import clear_tags
from lessons_with_desc import build_lesson_with_desc_type


lesson_pattern = r"<p>.*?<\/p>|<p>.*?<br>|.*?<\/p>|<li>.*?<\/li>"
regex_priorities = (
    r"<li>.*?<\/li>",
    r"<p>.*?<\/p>|<p>.*?<br>|.*?<\/p>"
)


def build_lesson_type(program: str) -> str:
    """Как должна выглядеть программа без модулей:
        [
            {
                "name" : "",
                "lessons": [
                    {
                        "name": "Урок 1 (или его название) ",
                        "desc": "Описание урока 1"
                    },
                    .......
                    {
                        "name": "Урок n (или его название) ",
                        "desc": "Описание урока n"
                    },
                ]
            },
        ]

        0] => [
        ‘name’ => ‘’,
        ‘lessons’ => [
            0 => [
                ‘name’ => ‘Урок 1 (или его название) ’,
                ‘desc’ => ‘Описание урока 1’
    ],
    …
    n => [
        ‘name’ => ‘Урок n (или его название) ’,
        ‘desc’ => ‘Описание урока n’
    ]
    ]
    ],
    """
    
    if "<strong>" in program: return build_lesson_with_desc_type(program)
    
    for pattern in regex_priorities:
        finded = re.findall(pattern, program)
        if finded:
            break

    lessons: list[dict] = []
    for lesson in finded:
        lesson = clear_tags(lesson)
        if not lesson or "Программа курса" in lesson: continue
        lessons.append({
            "name": clear_tags(lesson),
            "desc": ""
        })
    return [{
        "name": "",
        "lessons": lessons
    }]
        


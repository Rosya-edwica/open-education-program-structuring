import re
import os

from lessons import build_lesson_type
from module import build_module_type
from storage import *


def bring_program_to_single_structure(program: str) -> str:
    if re.findall("Раздел |Тема \d+|Модуль |РАЗДЕЛ ", program):
        return build_module_type(program)
    else:
        return build_lesson_type(program)

def update_programs(programs: list[dict]) -> list[dict]:
    result: list[dict] = []
    for item in range(len(programs)):
        updated = bring_program_to_single_structure(programs[item])
        if updated == []: # Проверяем, получилось вытащить программу или нет
            print(programs[item])
            exit(f"Failed {item}") 
        print(item)
        save_program_json(updated, filename=item)
        save_program_txt(programs[item], filename=item)
        result.append(updated)
    return result
        

if __name__ == "__main__":
    os.makedirs("debugging/JSON", exist_ok=True)
    os.makedirs("debugging/PROGRAMS", exist_ok=True)
    
    programs = load_programs()
    updated = update_programs(programs)
    save_updated_programs(updated)
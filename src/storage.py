import csv
import json


COLUMN_PROGRAM = 14

def load_programs(path: str = "input/course_202303080911.csv") -> list[str]:
    programs: list[str] = []
    with open(path, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(reader):
            if i == 0: continue
            programs.append(row[COLUMN_PROGRAM])
    return programs


def save_updated_programs(programs: list[str], path: str = "output/course_202303080911.csv") -> None:
    rows = merge_rows_with_program(programs, path)
    
    with open(path, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerows(rows)

def merge_rows_with_program(programs: list[str], path :str = "output/course_202303080911.csv") -> list[list[str]]:
    rows: list[list[str]] = []
    with open(path, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(reader):
            if i == 0:
                rows.append(row)
                continue
            row[COLUMN_PROGRAM] = programs[i-1]
            rows.append(row)
    return rows


def save_program_txt(program: str, filename: str):
    with open(f"debugging/PROGRAMS/{filename}.txt", mode="w", encoding="utf-8") as file:
        file.write(program)

def save_program_json(program: str, filename: str):
    with open(f"debugging/JSON/{filename}.json", mode='w', encoding="utf-8") as file:
        json.dump(program, file, indent=2, ensure_ascii=False)
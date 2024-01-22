import pandas as pd
from collections import Counter
from openpyxl import Workbook


def counter_skills(vacancies):
    skills_counter = Counter()

    profession_data = vacancies

    skills_lists = (
        profession_data["key_skills"]
        .dropna()
        .str.replace("\r", "")
        .str.split('\n')
    )

    skills_counter.update([skill for skills_list in skills_lists for skill in skills_list])
    top_skills = skills_counter.most_common(20)
    return top_skills


def create_skill_tab(wb: Workbook, data: list) -> None:
    wb_skills = wb["Sheet"]
    wb_skills.title = 'ТОП-20 навыков'
    wb_skills.append(['Навык', 'Количество навыков'])

    for values in data:
        left = values[0]
        right = values[1]

        wb_skills.append([left, right])


def main() -> None:
    vacancies = pd.read_csv('vacancies_ios.csv')
    skills = counter_skills(vacancies)
    wb = Workbook()
    create_skill_tab(wb, skills)
    wb.save('table_skills_ios.xlsx')


if __name__ == "__main__":
    main()

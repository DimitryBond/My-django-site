import re
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


def main() -> None:
    file_path = 'vacancies_ios.csv'
    data = pd.read_csv(file_path)
    data['published_at'] = data['published_at'].apply(
        lambda x: re.search(r'\d{4}', str(x)).group() if pd.notna(x) else None)

    wb = Workbook()
    create_years_tab(wb, data)

    wb.save('table_demand_ios.xlsx')


def create_years_tab(wb: Workbook, data: pd.DataFrame) -> None:
    wb_years = wb["Sheet"]
    wb_years.title = 'Статистика по годам'
    wb_years.append(['Год', 'Средняя зарплата', 'Количество вакансий'])

    # посчитать средние зарплаты
    def calculate_average_salary(group):
        return round(group[['salary_from', 'salary_to']].mean().mean())

    grouped_data = (
        data.groupby('published_at')
        .apply(calculate_average_salary)
        .reset_index()
    )

    for row in dataframe_to_rows(grouped_data, index=False, header=False):
        year = row[0]
        avg_salary = row[1]
        num_vacancies = len(data[data['published_at'] == year])
        wb_years.append([year, avg_salary, num_vacancies])


if __name__ == "__main__":
    main()

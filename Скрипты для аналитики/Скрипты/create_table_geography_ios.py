import re
import pandas as pd
from openpyxl import Workbook


def main() -> None:
    file_path = 'vacancies_ios.csv'
    data = pd.read_csv(file_path)
    data['published_at'] = data['published_at'].apply(
        lambda x: re.search(r'\d{4}', str(x)).group() if pd.notna(x) else None)

    wb = Workbook()
    create_cities_tab(wb, data)

    wb.save('table_geography_ios.xlsx')


def create_cities_tab(wb: Workbook, data: pd.DataFrame) -> None:
    wb_cities = wb["Sheet"]
    wb_cities.title = 'Статистика по городам'
    wb_cities.append(["Город", "Уровень зарплат", "", "Город", "Доля вакансий, %"])

    cities = (
        data['area_name'].value_counts(normalize=True)
        .reset_index(name='Percent')
    )
    filtered_cities = cities[cities['Percent'] > 0.01]

    def calculate_average_salary(group):
        area_name = group['area_name'].iloc[0]
        if area_name in filtered_cities['area_name'].values:
            return int(round(group[['salary_from', 'salary_to']].mean().mean()))

    cities_salary = (
        data.groupby('area_name')
        .apply(calculate_average_salary)
        .reset_index(name='Average')
        .sort_values(by='Average', ascending=False)
        .head(10)
    )

    cities_percent = (
        filtered_cities.head(10)
        .sort_values(by=['Percent', 'area_name'], ascending=[False, True])
    )

    for values in zip(cities_salary.values, cities_percent.values):
        left = values[0]
        right = values[1]
        percent = round(right[1] * 100, 2)
        wb_cities.append([left[0], left[1], "", right[0], percent])


if __name__ == "__main__":
    main()

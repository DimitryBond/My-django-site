import csv


def universal_csv_parser(file_name: str) -> list:
    vacancies = []
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        list_naming = next(reader, [])

        for row in reader:
            if len(row) == len(list_naming) and ('' not in row):
                vacancy = dict(zip(list_naming, row))
                if 'ios' in vacancy['name'].lower():
                    vacancy = convert_salary(vacancy)
                    vacancies.append(vacancy)

    return vacancies


def write_file(vacancies_data: list):
    with open('vacancies_ios.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(["name", "key_skills", "salary_from",
                    "salary_to", "salary_currency", "area_name", "published_at"])

        for item in vacancies_data:
            w.writerow(item.values())


def convert_salary(vacancy: dict) -> dict:
    currency_to_rub = {
        "AZN": 35.68,
        "BYR": 23.91,
        "EUR": 59.90,
        "GEL": 21.74,
        "KGS": 0.76,
        "KZT": 0.13,
        "RUR": 1,
        "UAH": 1.64,
        "USD": 60.66,
        "UZS": 0.0055,
    }

    salary_from = float(vacancy.get("salary_from", 0))
    salary_to = float(vacancy.get("salary_to", 0))
    salary_currency = vacancy.get("salary_currency", "RUR")

    if salary_currency != "RUR":
        salary_from *= currency_to_rub.get(salary_currency, 1)
        salary_to *= currency_to_rub.get(salary_currency, 1)

    vacancy['salary_from'] = salary_from
    vacancy['salary_to'] = salary_to
    vacancy['salary_currency'] = "RUR"

    return vacancy


if __name__ == "__main__":
    data = universal_csv_parser("vacancies.csv")
    write_file(data)

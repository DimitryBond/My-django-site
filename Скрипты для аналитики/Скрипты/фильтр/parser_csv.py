import csv
import pandas


def universal_csv_parser(file_name: str) -> list:
    vacancies = []
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        list_naming = next(reader, [])

        for row in reader:
            if len(row) == len(list_naming) and ('' not in row):
                vacancy = dict(zip(list_naming, row))
                vacancies.append(vacancy)

    return vacancies


def write_file(data: list):
    # df = pandas.DataFrame(columns=["index", "name", "key_skills", "salary_from",
    #                                "salary_to", "salary_currency", "area_name", "published_at"])
    #
    # for num, value in enumerate(data):
    #     df.loc[num] = [value.get('')]
    #
    # df.to_csv(r"current_ios_vacancies.csv", index=False, header=False)

    with open('data.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(["index", "name", "key_skills", "salary_from",
                    "salary_to", "salary_currency", "area_name", "published_at"])
        # for element in data:
        #     for key in element.keys():
        #         w.writerow([element[key]])

        for item in data:
            w.writerow(item.values())
        # w.writerows(data)


if __name__ == "__main__":
    data = universal_csv_parser("ios_vacancies.csv")
    write_file(data)

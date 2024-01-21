import pandas as pd


# name,key_skills,salary_from,salary_to,salary_currency,area_name,published_at
vacancies = pd.read_csv('../vacancies.csv', dtype={"name": "string", "key_skills": "string",
                                                "salary_from": float, "salary_to": float,
                                                "salary_currency": "string", "area_name": "string",
                                                "published_at": "string"})

filter_vacancies = vacancies[vacancies["name"].str.contains("ios", case=False)]
filter_vacancies.to_csv(r'ios_vacancies.csv')


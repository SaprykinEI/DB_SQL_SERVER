import json

import requests


class HH:

    employers_data = []
    vacancies_emp = []

    def __init__(self, employer):
        self.employer = employer
        self.employer_dict = {}
        self.vacancies_emp = []

    def get_employer(self):
        url = r'https://api.hh.ru/employers'
        params = {'text': {self.employer}, 'areas': 113, 'per_page': 20}
        response = requests.get(url, params)
        employer = response.json()

        if not employer:
            print("Данные не получены")
            return False
        elif not employer['items']:
            print("Нет указанных работадателей")
            return False
        else:
            for emp in employer['items']:
                self.employer_dict = {
                    'id': emp['id'],
                    'name': emp['name'],
                    'alternate_url': emp['alternate_url']
                }
                HH.employers_data.append(self.employer_dict)

    def __get_page_vacancies(self, employer_id, page):
        params = {
            'employer_id': employer_id,
            'area': 113,
            'per_page': 100,
            'page': page
        }
        response = requests.get('https://api.hh.ru/vacancies', params)
        data = response.content.decode()
        response.close()
        return data


    def get_vacancies(self, employer_id):
        vacancies_emp_dicts = []
        for page in range(10):
            vacancies_data = json.loads(self.__get_page_vacancies(employer_id, page))
            if 'errors' in vacancies_data:
                print(vacancies_data['errors'][0]['value'])
            for vacancy_data in vacancies_data['items']:
                if vacancy_data['salary'] is None:
                    vacancy_data['salary'] = {}
                    vacancy_data['salary']['from'] = None
                    vacancy_data['salary']['to'] = None
                vacancy_dict = {
                    'id': vacancy_data['id'],
                    'city': vacancy_data['area']['name'],
                    'vacancy': vacancy_data['name'],
                    'url': vacancy_data['alternate_url'],
                    'salary_from': vacancy_data['salary']['from'],
                    'salary_to': vacancy_data['salary']['to'],
                    'employer_id': vacancy_data['employer']['id'],
                }
                self.vacancies_emp.append(vacancy_dict)
        return  self.vacancies_emp







if __name__ == '__main__':
    hh = HH('skyeng')
    print(hh.get_employer())
    print(HH.employers_data)
    print(len(hh.get_vacancies('1122462')))

import requests
from random import randint
from bs4 import BeautifulSoup
from time import sleep

from read_book import import_data
from headers import get_header

url = 'https://companies.rbc.ru/search/?query='
check_error = "По вашему запросу ничего не найдено"


def get_data():
    header = None
    for id_comp in import_data():

        # если ИНН пустой - переходим к следующему
        if not id_comp:
            continue

        sleep(randint(2, 4))
        # Если ИНН меньше 10 цифр, добавляем впереди нули
        id_comp = str(id_comp).rjust(10, "0")

        try:
            response = requests.get(f"{url}{id_comp}", headers=header)
            # print(f"Статус ответа - {response.status_code}")
        except Exception as e:
            print(e)
            header = get_header()
            continue

        soup = BeautifulSoup(response.text, 'lxml')

        # Проверяем на ошибку поиска ИНН
        check = soup.find("p").text
        if check_error in check:
            yield {1: "ИНН не найден",
                   2: id_comp}
            continue

        # Активная ли компания?
        active = soup.find("span", class_="company-status-badge").text

        # наименование компании
        name = soup.find("a", class_="company-name-highlight").find("span").text

        # полное наименование
        full_name = soup.find("a", class_="company-name-highlight").find("span").get("title")

        # Род деятельности
        categories = soup.find("div", class_="category-breadcrumb")
        lst = []
        try:
            for cat in categories:
                if len(cat.text) > 1:
                    lst.append(cat.text.strip())
            category = lst[-1]
        except TypeError:
            category = "Нет данных"

        # достаем остальную нужную информацию
        company_info = soup.find_all("p", class_="company-card__info")
        info_comp = {}
        for info in company_info:
            try:
                items = info.text.split(":")
                info_comp[items[0]] = items[1]
            except IndexError:
                continue

        inn = id_comp
        address = info_comp.get("Юридический адрес")
        growth_rate = info_comp.get("Темп прироста")
        revenue = info_comp.get("Выручка")

        yield [active,
               inn,
               name,
               full_name,
               category,
               address,
               revenue,
               growth_rate]


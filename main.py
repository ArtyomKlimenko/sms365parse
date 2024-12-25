import requests

def get_cheapest_sms(api_key, country):
    # URL для получения списка цен
    url = "https://365api.net/stubs/handler_api.php"

    # Параметры запроса
    params = {
        "api_key": api_key,
        "action": "getPrices",
        "service": 'tg',
        "country": country
    }

    try:
        # Отправляем GET-запрос
        response = requests.get(url, params=params)
        #print(response)
        response.raise_for_status()

        # Получаем JSON-ответ
        data = response.json()
        # Проверяем наличие данных
        min_cost = 10000.0
        if not data:
            print("Нет данных о ценах.")
            return
        else:
            #min_cost = data[0][0][0]

                return data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except ValueError:
        print("Ошибка обработки JSON.")

# Использование функции
api_key = "NO_KEY"  # Замени на свой API-ключ
i = 0
min_cost = 10000
while True:
    data_p = get_cheapest_sms(api_key, i)

    try:
        if float((data_p[str(i)]['tg']['cost'])) < min_cost+50:
            min_cost = float((data_p[str(i)]['tg']['cost']))+50
            print(data_p)
    except TypeError:
        print('none')
     i += 1

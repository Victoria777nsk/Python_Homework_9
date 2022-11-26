import requests                               # Библиотека requests для обращения к сайту.
from bs4 import BeautifulSoup                 # Библиотека BeautifulSoap для поиска нужных данных на сайте.

weather = 'https://world-weather.ru/pogoda/russia/novosibirsk/'

r = requests.get(weather)                     # Переменная для передачи запросов.
soup = BeautifulSoup(r.text, 'html.parser')   # Присваиваем параметры парсера (сборщика данных с сайта).

for temp in soup.find_all('div', id = 'weather-now-number'):
    temp = temp.text                          # Присваиваем переменной temp полученное значение температуры воздуха.

for obl in soup.find_all('span', id = 'weather-now-icon'):
    obl = obl.get('title')                    # Цикл для получения осадков и облачности.

for timew in soup.find_all('div', class_ = 'weather-now-info'):
    timew = timew.text[6:-7]                  # Цикл для времени и даты прогноза, убираем лишние символы (6 в начале и 7 с конца).

for dr in soup.find_all('div', id = 'weather-now-description'):
    line = dr.text
    last_index = 0
    itog = []
    for i, char in enumerate(line[1:-9]):
        if char.istitle() or i == len(line[1:-10]):
            itog.append(line[last_index:i + 1])
            last_index = i + 1
    itog.append(line[-10:-4])
    itog.append(line[-4])
    dr = ' '.join(itog[:-5])

send_tg = 'Погода в Новосибирске: ' + '\n' + temp + ' ' + obl + '\n' + dr + '\n' + 'Данные на: ' + timew
print(send_tg)

bot = '5690611072:AAHQvxwHqX8eCEeYkeqWi9AxCFS_R_1dAf0'
requests.get('https://api.telegram.org/bot{}/sendMessage'.format(bot), params = dict(chat_id = '1001650196036', text = send_tg))

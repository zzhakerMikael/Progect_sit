import random
from flask import Flask

app = Flask(__name__)

facts_list = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.", "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.", "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]

@app.route("/")
def hello_world():
    return f'<h1>Привет! Переходи по ссылке и узнай пару новых фактов!</h1>  <a href="/random_fact">Посмотреть случайный факт!</a>  <h2>Перейди по сылке ниже и сыграй в игру на удачу!</h2>  <a href="/Game1">Сыграть в игру!!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/Game1")
def game1():
    result1 = random.randint(1, 1000000)
    color1 = ""
    if result1 < 1000001 and result1 > 99999:
        color1 = "синий!"
    elif result1 < 100000 and result1 > 1:
        color1 = "Красный!!"
    elif result1 == 1:
        color1 = "ЗОЛОТОЙ!!!!!!!!!!!!!!"
    return f'<img src="https://downloader.disk.yandex.ru/preview/a062cdc745e2eaffbaecc6c8996789a5305335b984918d5c7fbfc3ad8f383a98/670c1568/oa7L-jVF_FwjhHZuM3AFyLFJZiIm51n8m-RE5GbS44hqh0fcPeDIWYAWwT280fFt3Otjb_D9Yu26ldRY506kcg%3D%3D?uid=0&filename=P_GAME1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1872x932" width="500" height="500" alt="Подсказка! Как играть!">  <h1>Вы выбили: {color1}</h1>  <a href="/">Назад!</a>'

app.run(debug=True)

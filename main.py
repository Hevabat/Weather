import requests
import datetime
s_city = "Moscow,RU"
city_id = 524901
appid = "abcf51d79e8e4cc10433106985e967dc"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Прогноз погоды на сегодня: \r\nГород:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'],"градусов Цельсия")
print("Минимальная температура:", data['main']['temp_min'],"градусов Цельсия")
print("Максимальная температура", data['main']['temp_max'],"градусов Цельсия")
print("Скорость ветра", data['wind']['speed'],"метров в секунду")
print("Видимость", data['visibility'], "метров")
print("***********************************")

res = requests.get("http://api.openweathermap.org/data/2.5/onecall",
    params={'lat' : '55.7522', 'lon' : '37.6156' , 'units': 'metric', 'lang': 'ru',  'APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['daily']:

    UT = i['dt']
    DT = datetime.datetime.fromtimestamp(UT)

    print("Дата <", DT,
          "> \r\nТемпература <", '{0:+3.0f}'.format(i['temp']['day']),
          " градусов Цельсия> \r\nПогодные условия <", i['weather'][0]['description'],
          "> \r\nСкорость ветра <", i['wind_speed'], "метров в секунду>")
    print("____________________________")

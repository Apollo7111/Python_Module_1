# 07bba31066e8e1fc064a6fd3717c5129
import requests

key = "07bba31066e8e1fc064a6fd3717c5129"
city = input("City: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"
try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()

        print(json_response["weather"][0]["description"])
        print(json_response["main"]["temp"],'Celcius')
except requests.exceptions.RequestException as e:
    print(e.args)
    print("Request could not be completed.")
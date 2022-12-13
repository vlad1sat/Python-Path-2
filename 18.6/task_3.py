import requests
import json


my_req = requests.get('https://www.breakingbadapi.com/api/deaths')
print(my_req.text)
# ОШИБКА ПОЛУЧЕНИЯ ДАННЫХ
# {"name":"error","length":118,"severity":"FATAL","code":"28000","file":"miscinit.c","line":"716","routine":"InitializeSessionUserId"}
# Невозможно получить данные с сайта, возникает ошибка 500. Из-за этого нельзя их обработать
# Даже в режиме playground невозможно их получить


import requests

files = {'file': open("C:/analiza/week14/week_14_test/data/weapons_list.csv", 'rb')}


response = requests.post('http://localhost:8000/upload', files=files)

import json
import requests
from pprint import pprint

with open("test.json", "r") as f:
        data = json.load(f)

with open("data.json", "w") as f:
    data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    json.dump(data, f, indent=4)

data2 = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()

pprint(data2)


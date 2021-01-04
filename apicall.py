import json
import requests

with open("data.json", "w") as f:
    data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    json.dump(data, f, indent=4)
    
variable = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        




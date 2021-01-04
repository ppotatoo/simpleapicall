import json
import requests

with open("data.json", "w") as f:
    data = requests.get('https://www.beatsavior.io/api/livescores/player/3032736043471367').json()
    json.dump(data, f, indent=4)
    
variable = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()

with open("data.json", "r") as f:
        data = json.load(f)


for data in data[0:5]:
	print('Name: \''+data['songName']+'\' Difficulty: \''+data['songDifficulty']+'\'')

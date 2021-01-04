import json
import requests

def choice():
	c = input('Would you like to use ScoreSaber or BeatSavior. Please type carefully. \n')
	if c == 'ScoreSaber':
		scoresaber()
	if c == 'BeatSavior':
		beatsavior()

def beatsavior():
	uid = int(input('Insert your ScoreSaber ID: \n'))

	with open("data.json", "w") as f:
		data = requests.get(f'https://www.beatsavior.io/api/livescores/player/{uid}').json()
		json.dump(data, f, indent=4)

	with open("data.json", "r") as f:
		data = json.load(f)

	for data in data[0:5]:
		print(f"Name: {data['songName']} Difficulty: {data['songDifficulty']}")

def scoresaber():
	uid = (input('Insert your ScoreSaber ID: \n'))

	with open("data.json", "w") as f:
		data = requests.get(f'https://new.scoresaber.com/api/player/{uid}/full').json()
		json.dump(data, f, indent=4)

	with open("data.json", "r") as f:
		data = json.load(f)
	
	print(f"Name: {data['playerInfo']['playerName']} Rank: {+data['playerInfo']['rank']}")

choice()

import json
import requests

async def choice():
	c = input('Would you like to use ScoreSaber or BeatSavior. Please type carefully.')
	if c == 'ScoreSaber':
		scoresaber()
	if c == 'BeatSavior':
		beatsavior()

async def beatsavior():
	uid = int(input('Insert your ScoreSaber ID: \n'))

	with open("data.json", "w") as f:
    	data = requests.get(f'https://www.beatsavior.io/api/livescores/player/{uid}').json()
    	json.dump(data, f, indent=4)

	with open("data.json", "r") as f:
        data = json.load(f)


	for data in data[0:5]:
		print('Name: \''+data['songName']+'\' Difficulty: \''+data['songDifficulty']+'\'')

async def scoresaber():
	uid = int(input('Insert your ScoreSaber ID: \n'))

	with open("data.json", "w") as f:
    	data = requests.get(f'https://new.scoresaber.com/api/player/{uid}/full').json()
    	json.dump(data, f, indent=4)

	with open("data.json", "r") as f:
        data = json.load(f)
	
	print('Name: \''+data['songName']+'\' Difficulty: \''+data['songDifficulty']+'\'')

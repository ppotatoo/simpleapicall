import os
import requests
from pprint import pprint

def wipe():
    os.system("cls")

def scoresaber():
    uid = (input('Insert your ScoreSaber ID: \n'))
    wipe()
    data = requests.get(f'https://new.scoresaber.com/api/player/{uid}/full').json()
    print("\nPlayer Info:")
    print(f"    Player ID: {data['playerInfo']['playerId']}")
    print(f"    Player Name: {data['playerInfo']['playerName']}")
    print(f"    Avatar: https://new.scoresaber.com{data['playerInfo']['avatar']}")
    print(f"    Country: {data['playerInfo']['country']}")
    print(f"    Rank: {data['playerInfo']['rank']}")
    print(f"    Country Rank: {data['playerInfo']['countryRank']}")
    print(f"    Performance Points: {data['playerInfo']['pp']}")
    print(f"    Role: {data['playerInfo']['role']}")
    print("\nScore Stats:")
    print(f"    Total Score: {data['scoreStats']['totalScore']}")
    print(f"    Total Ranked Score: {data['scoreStats']['totalRankedScore']}")
    print(f"    Average Ranked Accuracy: {data['scoreStats']['averageRankedAccuracy']}")
    print(f"    Total Play Count: {data['scoreStats']['totalPlayCount']}")
    print(f"    Ranked Play Count: {data['scoreStats']['rankedPlayCount']}\n")
    scoresaber()
scoresaber()

#{data['playerInfo']
#print(f"")


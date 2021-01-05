# simpleapicall

## Some Sample API's
### ScoreSaber Top Songs: 
https://new.scoresaber.com/api/player/3032736043471367/scores/top/0
You can change 'top' to 'recent' and '0' to any number to filter through pages.
### ScoreSaber Profile
https://new.scoresaber.com/api/player/3032736043471367/full

You can change the player ID's to match anyone's.

### BeatSavior Recent Songs
https://www.beatsavior.io/api/livescores/player/3032736043471367

You have to filter carefully throught it, as there is a lot of info, but it's worth it.
Again, the player ID can be changed, but the player has to have the BeatSavior mod installed.

### BeatSaver Song Data
https://beatsaver.com/api/maps/detail/6666
You have to define a user agent, a simple Google search should be good enough.

Docs: https://docs.beatsaver.com/endpoints/
The data is unformatted, you will have to format it with something like pretty print in Python, or a JSON formatter.

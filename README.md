# Brawl Stars v36

Experimental Brawl Stars v36.218 server emulator written in Python.

![ScreenShot](https://cdn.discordapp.com/attachments/704364452891590778/885467610400051200/Screenshot_20210909-131154_BS_v36.jpg) 

### Requirements:
- Python 3.7 or higher
- colorama

### Running the server
In a terminal, type __`pip install -r requirements.txt`__ then run the server using __`python main.py`__

### Configuring the client app
To connect to your server, a **patched client** is required. Download this [base APK](https://mega.nz/file/7DByET5J#mVfDFli2dw1gdoDUROMkXWHolFicCX5_g2tXzXRiK3s) and change the IP in `libmg.config.so`. 

⚠️ This client is unstable and might crash sometimes. It is not recommended to use it for a production environment.
### Battles
We've enabled offline battles so you can directly press "PLAY" to start a match.
![ScreenShot](https://cdn.discordapp.com/attachments/704364452891590778/885473792208543774/Screenshot_20210909-133614_BS_v36.jpg) 
Unfortunately, the offline logic is mostly broken and some gamemodes/brawlers might crash the game or not work correctly. 
After multiple tests we've made it appears these 3 gamemodes still behave normally:
- Gem Grab
- Bounty
- Big Game

You'll find some maps we've selected for you in the events tab.
![ScreenShot](https://cdn.discordapp.com/attachments/704364452891590778/885475373175939132/Screenshot_20210909-134247_BS_v36.jpg) 

### Got any question?
Contact @ShockWave#5158 on Discord or open an issue.

### Important Notice
This is an experimental and incomplete server made just for fun. No database, no data saving. 
The purpose of this project is to prove that making a private server for Brawl Stars is still possible.
We won't provide further updates nor will we offer support for miss-features or other issues.

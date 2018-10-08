# MADBot
This is a Bot written in Python3.6 that downloads user-submitted images on Discord for Map-A-Droid.  
If you prefer JavaScript, [MADBot](https://github.com/LegitDongo/MADBot)
## Requirements:  
* [Map-A-Droid](https://github.com/Grennith/Map-A-Droid)  
* Python3.6

## How to use:
1. Clone the repository `git clone https://github.com/OfficialWiddin/MADBot_Python.git`  

2. Install the requirements `python -m pip install -r requirements.txt`  

3. Copy `config.ini.example` and rename it to `config.ini`  
    * **Token:**
        * [Discord Developer Applications](https://discordapp.com/developers/applications/) and click `Create an application` 
        * Click on the `Bot` tab on the left side and then `Add Bot`. 
        * Click on `Copy` under the `TOKEN`, paste into `config.ini` 
        
    * **Channel_id:**
        * Open `User settings` on Discord. 
        * Go `Appearance` and enable `Developer Mode`
        * Right click on the chosen channel and choose `Copy ID`, paste into `config.ini`


    * **Screenshot_path:**
        * Locate the screenshot folder within Map-A-Droid with the terminal, run `pwd`, paste into `config.ini`
        
4. Replace `YOUR_CLIENT_ID_HERE` in `https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=0` with your `CLIENT ID` which can be found on `General Information` tab on the [application site](https://discordapp.com/developers/applications/). Then paste the link in your browser and select your server.
        
5. Run the bot with `python start_bot.py`

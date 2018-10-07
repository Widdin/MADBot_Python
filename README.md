# MADBot

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
        
4. Run the bot with `python start_bot.py`

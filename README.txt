☀️ Telegram Weather Bot with OpenWeatherMap API

Want instant and accurate weather updates? This bot provides real-time weather forecasts directly in Telegram, powered by OpenWeatherMap API!
Get the latest temperature, weather conditions, and forecasts for any city worldwide—fast and hassle-free.

✅ What does it do?

 • 🌍 Provides weather updates for any city
 • 🌡️ Shows real-time temperature, humidity, wind speed, and more
 • 📅 Offers multi-day forecasts
 • 📌 Saves favorite locations for quick access

🔧 Features

✅ Fast and accurate weather reports powered by OpenWeatherMap API
✅ Simple and user-friendly interface
✅ Multi-city support for tracking different locations

📩 Want to stay updated on the weather anytime?

Contact me on Telegram, and I’ll help you set up this bot for instant weather updates! 🚀

=== HOW TO LAUNCH A TELEGRAM WEATHER BOT ===

This is a step-by-step guide for running the Weather Telegram bot on Windows and Linux.
Follow the instructions for your operating system.

=====================================================================
                         WINDOWS
=====================================================================

1. INSTALL PYTHON (VERSION 3.10)
--------------------------------
- Go to the website: https://www.python.org/downloads/release/python-31011/
- Scroll down the page and download the "Windows installer (64-bit)"
file - Run the downloaded file
- IMPORTANT: Check the box "Add Python 3.10 to PATH" during installation!
- Click "Install Now" and wait for the installation to finish

2. CHECKING THE PYTHON INSTALLATION
---------------------------
- Press Win + R on your keyboard
- Write "cmd" and press Enter
- In the command prompt that opens, type:
python --version
- You should see something like "Python 3.10.11"

3. GETTING API KEYS
----------------------
a) Receiving Telegram Bot Token:
- Open Telegram
- Find @BotFather and write to him
   - Send a command /newbot
   - Follow the instructions to give your bot a name.
   - Save the received token (looks like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11)

b) Getting the OpenWeatherMap API Key:
- Go to the website https://openweathermap.org /
- Click "Sign Up" and create an account
   - After registration, go to "My API keys"
- Save the API key (or create a new one)

4. DOWNLOADING THE BOT FILES
------------------------
- Create a new folder on your computer, for example, "weather-bot"
- Save the files main.py , config.py and README.md to this folder

5. SETTING UP THE BOT
---------------
- Open the config file.py using notepad (right-click on the file -> Open with -> Notepad)
- Replace "YOUR_TELEGRAM_BOT_TOKEN" with the token received from @BotFather
- Replace "YOUR_OPENWEATHERMAP_API_KEY" with the key from OpenWeatherMap
- Save the file (Ctrl+S)

6. INSTALLING DEPENDENCIES
-----------------------
- Return to the command prompt (or open a new one: Win + R -> cmd -> Enter)
- Enter the command to go to the folder with the bot files:
  cd path to your folder For

example:
  cd C:\Users\ИмяПользователя\Documents\weather-bot
  
- Install the necessary libraries with the command:
pip install aiogram==3.0.0 aiohttp

7. LAUNCHING THE BOT
------------
- At the command prompt, type:
python main.py
- If everything is done correctly, you will see messages about the launch of the bot.
- The bot will work while the command prompt is open

8. USING A BOT
------------------
- Open Telegram
- Find your bot by the name you gave when creating it.
- Send the command /start
- To find out the weather, write "weather" and the name of the city (for example, "weather Moscow")

=====================================================================
                            LINUX
=====================================================================

1. INSTALL PYTHON (VERSION 3.10)
--------------------------------
- Open a terminal (Ctrl+Alt+T in most distributions)
- Enter the following commands:

  For Ubuntu/Debian:
  sudo apt update
  sudo apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt update
  sudo apt install python3.10 python3.10-venv python3-pip

  For Fedora:
  sudo dnf install python3.10

  For CentOS/RHEL:
  sudo yum install python3.10

2. CHECKING THE PYTHON INSTALLATION
---------------------------
- In the terminal, type:
python3.10 --version
- You should see "Python 3.10.x"

3. GETTING API KEYS
----------------------
a) Receiving Telegram Bot Token:
- Open Telegram
- Find @BotFather and write to him
   - Send a command /newbot
   - Follow the instructions to give your bot a name
- Save the received token

b) Getting the OpenWeatherMap API Key:
- Go to the website https://openweathermap.org /
- Click "Sign Up" and create an account
   - After registration, go to "My API keys"
- Save the API key (or create a new one)

4. DOWNLOADING THE BOT FILES
------------------------
- Create a new folder with the command:
mkdir ~/weather-bot
- Go to the folder:
  cd ~/weather-bot
- Create files with commands:
  nano main.py
(insert the code from main.py , then Ctrl+O to save, Enter, and Ctrl+X to exit)

nano config.py
(insert the code from config.py , then Ctrl+O to save, Enter, and Ctrl+X to exit)

5. SETTING UP THE BOT
---------------
- Open it config.py :
nano config.py
- Replace "YOUR_TELEGRAM_BOT_TOKEN" with the token received from @BotFather
- Replace "YOUR_OPENWEATHERMAP_API_KEY" with the key from OpenWeatherMap
- Save the file: Ctrl+O, then Enter, then Ctrl+X

6. CREATING A VIRTUAL ENVIRONMENT AND INSTALLING DEPENDENCIES
--------------------------------------------------------
- In the terminal, run the following commands:
python3.10 -m venv venv
  source venv/bin/activate
  pip install aiogram==3.0.0 aiohttp

7. LAUNCHING THE BOT
------------
- In the terminal, make sure that you have activated the virtual environment (it should be (venv) at the beginning of the line)
- If not, activate it:
source venv/bin/activate
- Launch the bot:
python main.py
- The bot will work while the terminal is open

8. RUNNING THE BOT IN THE BACKGROUND (OPTIONAL)
-------------------------------------------
- So that the bot does not stop when closing at the terminal, run:
nohup python main.py > bot_log.txt 2>&1 &
- To check if the bot is running:
ps aux | grep python

9. USING A BOT
------------------
- Open Telegram
- Find your bot by the name you gave when creating it.
- Send the command /start
- To find out the weather, write "weather" and the name of the city (for example, "weather Moscow")

=====================================================================
          POSSIBLE ERRORS AND THEIR SOLUTIONS
=====================================================================

1. "python is not an internal or external command..." (Windows)
   Solution: Make sure that you check the box "Add Python to PATH" during installation.
   Alternatively, use the full Python path or reinstall Python.

2. "ModuleNotFoundError: No module named 'aiogram'"
Solution: Make sure that you have installed the dependencies correctly with the pip install command.

3. "Failed to connect to the bot"
   Solution: Check the Internet connection and the correctness of the Telegram Bot Token.

4. "Error receiving weather data"
   Solution: Check the correctness of the OpenWeatherMap API Key and its activation.

5. For Linux: "Command 'python' not found"
   Solution: Use the python3 or python3.10 command instead of python.

=====================================================================
If you have any additional questions or problems, please
refer to the Python, aiogram, or OpenWeatherMap documentation.
=====================================================================

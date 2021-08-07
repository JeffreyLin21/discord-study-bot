# discord-study-bot

## Description

This is a Discord bot that was created to help users study. Written in Python using the Discord api. Designed to work in a private chat with Discord bot and not in a server.

The bot includes a study commands that sends messages to the user of when to study and when to take a break. This style of studying is a similar version of the [Pomodoro technique](https://www.youtube.com/watch?v=IUXNiDJJ_9s). 

Other features include a reminder feature that sends messages on a timer, a todo list feature, using Sqlite3, that can save and load todo lists even when Discord gets closed, as well as a youtube video search feature, using the YouTube Data api.

## Installation

Install Python with Sqlite3 and pip. Version that was used for this project was Python 3.9.6.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Discord and YouTube Data libaries.

https://discordpy.readthedocs.io/en/stable/intro.html
https://github.com/googleapis/google-api-python-client

```bash
pip install -U discord.py
pip install google-api-python-client
```

Set up your discord bot [here](https://discord.com/developers/applications/)
1. Create a new application
2. Enable all permissions in OAuth2 tab
3. Generate a token in the Bot tab
4. Paste the token in a txt file named 'token.txt' in the main repo folder

Set up the YouTube Data api [here](console.cloud.google.com)
1. Add a new project
2. Enable the YouTube Data Api v3
3. Get your api key from credentials
4. Paste the api key in a txt file named 'api.txt' in the main folder

Generate a link to add the bot to a server, run the main.py file, and finally use any commands with the bot to get started. 

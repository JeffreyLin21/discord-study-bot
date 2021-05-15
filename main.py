import os
import discord
import requests
import json

client = discord.Client()  

@client.event
async def on_ready():
  print('Hello Jeffury is ready to help you study'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith('!quit'):
    await message.channel.send('Quitting')

client.run(os.environ['token'])
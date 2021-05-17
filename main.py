import os
import discord
import time
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!') 

@client.command(name='study')
async def study(context):

  global isStudying
  change = -1
  isStudying = True
  state = 1    
  start = time.time() 
  command = context.message.content.split()
  channel = context.message.channel

  try:

    if len(command) == 1:
      studyTime = 30
      breakTime = 5
      cycles = 4
    elif len(command) == 3:
      studyTime = int(command[1]) * 60
      breakTime = int(command[2]) * 60    
      cycles = 1
      change = 0
    elif len(command) == 4:
      studyTime = int(command[1]) * 60
      breakTime = int(command[2]) * 60     
      cycles =  int(command[3]) * 2

    study_embed = discord.Embed(title = 'Study Time!', description = ('Current session: ' + str(studyTime) + ' min remaining'))
    study_embed.set_footer(text = 'Type !status to check current timer')

    break_embed = discord.Embed(title = 'Break Time!', description = ('Current session: ' + str(breakTime) + ' min remaining'))
    study_embed.set_footer(text = 'Type !status to check current timer')
    
    end_embed = discord.Embed(title = 'Good session!')

    await channel.send(embed = study_embed)
    start = time.time()
    timer = studyTime
    
    while isStudying and cycles > 0:
      await asyncio.sleep(1)
      if (time.time() - start) >= timer:
        cycles = cycles + change
        if state == 1:
          state = 0
          timer = breakTime
          if isStudying and cycles > 0:
            await channel.send(embed = break_embed)
        else:
          state = 1
          timer = studyTime
          if isStudying and cycles > 0:
            await channel.send(embed = study_embed)
        start = time.time()
    await channel.send(embed = end_embed)
  except Exception as e: 
    print(e)
    await channel.send('!study [Duration of studying] [Duration of break] [Cycles]')
    await channel.send('Leave all field blank for recommened settings (30 5 4) or leave cycles blank for unlimited session')
  
@client.command(name='quit')
async def quit(context):
  global isStudying
  isStudying = False

@client.event
async def on_ready():
  print('Bot is online')

client.run(os.environ['token'])
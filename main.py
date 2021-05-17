import os
import discord
import time
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!') 

@client.command(name='study')
async def study(context):
  global isStudying
  command = context.message.content.split()
  channel = context.message.channel
  try:
    isStudying = True
    studyTime = int(command[1]) * 1
    breakTime = int(command[2]) * 1
    cycles = int(command[3]) * 2
    await channel.send('Study time!')
    start = time.time()
    timer = studyTime
    state = 1    

    while isStudying and cycles > 0:
      await asyncio.sleep(1)
      if (time.time() - start) >= timer:
        cycles = cycles - 1
        if state == 1:
          state = 0
          timer = breakTime
          if isStudying and cycles > 0:
            await channel.send('Break time!')
        else:
          state = 1
          timer = studyTime
          if isStudying and cycles > 0:
            await channel.send('Study time!')
        start = time.time()
    await channel.send('Good study session!')
  except:
    await channel.send('!study [Duration of studying] [Duration of break] [Cycles]')
    await channel.send('Recommended: !study 30 5 4')
  
@client.command(name='quit')
async def quit(context):
  global isStudying
  isStudying = False


@client.event
async def on_ready():
  print('Bot is online')

client.run(os.environ['token'])
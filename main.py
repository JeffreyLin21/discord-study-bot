import os
import discord
import time

client = discord.Client()  

@client.event
async def on_ready():
  print('Hello, Jeffury is ready to help you study'.format(client))

@client.event
async def on_message(message):

  global isStudying
  global onBreak
  global studyTime
  global breakTime
  global msg

  msg = message

  if message.author == client.user:
    return

  if message.content == '!quit':
    onBreak = False
    isStudying = False

  if message.content.startswith('!study'):
    isStudying = True
    onBreak = False
    command = message.content.split()
    studyTime = int(command[1] * 60)
    breakTime = int(command[2] * 60)

    if not studyTime.isdigit() or not breakTime.isdigit():
      await message.channel.send('Sorry I don\'t understand')
    else:
      await studySession()

async def breakSession():
  global onBreak
  global isStudying
  global start
  global breakTime
  global msg

  start = time.time()

  if onBreak:
    await msg.channel.send('Break Time!')

  while onBreak:
    print(time.time() - start)
    if (time.time() - start) >= breakTime:
      isStudying = True
      onBreak = False
      await studySession()
      break


async def studySession():
  global isStudying
  global onBreak
  global start
  global studyTime
  global msg

  start = time.time()

  if isStudying:
    await msg.channel.send('Study Time!')

  while isStudying:
    print(time.time() - start)
    if (time.time() - start) >= studyTime:
      isStudying = False
      onBreak = True
      await breakSession()
      break

client.run(os.environ['token'])
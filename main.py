import os
import discord
import time

client = discord.Client()  

@client.event
async def on_ready():
  print('Hello, Jeffury is ready to help you study'.format(client))

@client.event
async def on_message(message):

  global studyTime
  global breakTime
  global isStudying
  global msg

  msg = message

  if message.author == client.user:
    return

  if message.content == '!quit':
    isStudying = False
    await message.channel.send('Good study session!')

  if message.content.startswith('!study'):
    isStudying = True
    command = message.content.split()

    try:
      studyTime = int(command[1] * 1)
      breakTime = int(command[2] * 1)
      await message.channel.send('Study time!')
      await studySession()
    except:
      await message.channel.send('Sorry I don\'t understand')

async def studySession():
  global isStudying
  global onBreak
  global start
  global studyTime
  global msg

  start = time.time()
  timer = studyTime
  state = 1    

  while isStudying:
    if not isStudying:
      break
    if (time.time() - start) >= timer:
      if state == 1:
        state = 0
        timer = breakTime
        await msg.channel.send('Break time!')
      else:
        state = 1
        timer = studyTime
        await msg.channel.send('Study time!')
      start = time.time()

client.run(os.environ['token'])
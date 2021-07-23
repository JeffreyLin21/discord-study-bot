from collections import deque
import os
import discord
import time
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!') 
user_study_list = {}
client.remove_command('help')

# commands
@client.command(name = 'help')
async def help(context):
  help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

  help_embed.add_field(name = '!study [duration of study period] [duration of break] [number of cycles]', value = 'begin study session', inline = False)
  help_embed.add_field(name = '!study', value = 'Leave all field blank for recommened settings !study 30 5 4', inline = False) 
  help_embed.add_field(name = '!study [duration of study period] [duration of break]', value = 'Leave cycle field blank for infinite session', inline = False) 
  help_embed.add_field(name = '!quit', value = 'end current study session', inline = False) 
  help_embed.add_field(name = '!status', value = 'check timer of current study session', inline = False)

  await context.message.author.send(embed = help_embed) 

@client.command(name='start')
async def start(context):
  msg_embed = discord.Embed(title = 'Hello I am Study Bot', description = "created by Jeffrey Lin", color = 0x831b6d)
  await context.message.author.send(embed = msg_embed)

@client.command(name='status')
async def status(context):
  global start
  global timer
  print (timer-(time.time()-start))
  try:
    timer_embed = discord.Embed(title = 'Timer', description = str(int(timer-(time.time()-start)/60)) + ':' + str(int(round((((timer * 60)-(time.time()-start))%60), 0))) + ' minutes remaining', color = 0x831b6d)
  except:
    timer_embed = discord.Embed(title = 'Looks like a study session hasn\'t started yet.')
  await context.message.author.send(embed = timer_embed)

@client.command(name='study')
async def study(context, studyTime = 30, breakTime = 5, cycles = 4):

  global start
  global isStudying
  global timer
  isStudying = True
  state = 1    
  start = time.time() 
  author = context.message.author

  try:

    study_embed = discord.Embed(title = 'Study Time!', description = ('Current session: ' + str(int(studyTime)) + ':00' + ' min remaining'), color=0x831b6d)
    study_embed.set_footer(text = 'Type !status to check current timer')

    break_embed = discord.Embed(title = 'Break Time!', description = ('Current session: ' + str(int(breakTime)) + ':00' + ' min remaining'), color=0x831b6d)
    study_embed.set_footer(text = 'Type !status to check current timer')

    quit_embed = discord.Embed(title = 'Good session!', color=0x831b6d)

    await author.send(embed = study_embed)
    start = time.time()
    timer = studyTime
    
    while isStudying and cycles != 0:
      await asyncio.sleep(1)
      if ((time.time() - start)/60.0) >= timer:
        cycles -= 1
        if state == 1:
          state = 0
          timer = breakTime
          if isStudying and cycles > 0:
            await author.send(embed = break_embed)
        else:
          state = 1
          timer = studyTime
          if isStudying and cycles > 0:
            await author.send(embed = study_embed)
        start = time.time()
    await author.send(embed = quit_embed)
  except Exception as e: 
    print(e)
    if start == ' ':
      await author.send(embed = quit_embed)
    else:
      end_embed = discord.Embed(description = '!study [Duration of studying] [Duration of break] [Cycles]', color=0x831b6d)
      end_embed.set_footer(text = 'Leave all field blank for recommened settings !study 30 5 4 or leave cycles blank for an infinite session')
      await author.send(embed = end_embed)

@client.command(name='quit')
async def quit(context):
  global isStudying
  global start
  start = ' '
  isStudying = False

@client.command(name = 'remind')
async def remind(context, remind_time = 1, message = 'not sure why, but you created this reminder!'):
  current = time.time()
  reminder = 'Reminder: ' + message
  try:
    while (time.time() - current <= remind_time * 60):
      await asyncio.sleep(1)
    msg_embed = discord.Embed(description = message, color=0x831b6d)
    await context.message.author.send(embed = msg_embed)
  except Exception as e: 
    print(e)
    end_embed = discord.Embed(description = '!remind [Number of minutes to remind in] [Message to send]', color=0x831b6d)
    await context.message.author.send(embed = end_embed)

@client.group(name = 'todo')
async def todo(context):
  return

@todo.command(name = 'help')
async def help(context):
  msg_embed = discord.Embed(title = '!todo [subcommand]', description = 'subcommands: add, next, clear, list', color=0x831b6d)
  await context.message.author.send(embed = msg_embed)

@todo.command(name = 'add')
async def add(context, *topic):
  try: 

    msg = ''
    for i in topic:
      msg += i + ' '

    if (context.message.author in user_study_list):
      user_study_list[context.message.author].append(msg)
    else:
      user_study_list[context.message.author] = deque()
      user_study_list[context.message.author].append(msg)
    msg_embed = discord.Embed(description = "'" + msg[:-1] + "'" + ' has been added to the todo list', color=0x831b6d)
    await context.message.author.send(embed = msg_embed)
  except Exception as e:
    print(e)
    msg_embed = discord.Embed(description = 'Please enter something to study', color=0x831b6d)
    await context.message.author.send(embed = msg_embed)
  
@todo.command(name = 'next')
async def add(context):
  try: 
    if (not user_study_list[context.message.author]):
      msg_embed = discord.Embed(description = 'There are no more topics to cover!', color=0x831b6d)
    else:
      user_study_list[context.message.author].popleft()
      msg_embed = discord.Embed(description = user_study_list[context.message.author][0], color=0x831b6d)
    await context.message.author.send(embed = msg_embed)
  except Exception as e:
    print(e)
    msg_embed = discord.Embed(description = 'Hm... looks like something went wrong', color=0x831b6d)
    await context.message.author.send(embed = msg_embed)

@todo.command(name = 'clear')
async def clear(context, limit = -1):
  try: 
    if limit == -1:
      user_study_list[context.message.author].clear()
    else:
      for i in range(0, limit):
        user_study_list[context.message.author].popleft()
    msg_embed = discord.Embed(description = 'Topics have been cleared!', color=0x831b6d)
    await context.message.author.send(embed = msg_embed)
  except Exception as e:
    print(e)
    msg_embed = discord.Embed(title = '!todo clear [number of topics to clear]', description = 'Leave last field blank to clear all', color=0x831b6d)
    await context.message.author.send(embed = msg_embed)

@todo.command(name = 'list')
async def list(context):
  try: 
    msg = str(user_study_list[context.message.author])
    msg_embed = discord.Embed(description = msg[7: -2], color=0x831b6d)
    await context.message.author.send(embed = msg_embed)
  except Exception as e:
    print(e)
    msg_embed = discord.Embed(description = 'Hm... looks like you don\'t have a list', color=0x831b6d)
    await context.message.author.send(embed = msg_embed)

@client.event
async def on_ready():
  print('Bot is online')

token = open("token.txt", "r")
client.run(token.read())


# dictionary = {user id, ['list', 'of', 'items']}
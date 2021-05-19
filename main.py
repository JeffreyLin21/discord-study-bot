import os
import discord
import time
import asyncio
from discord.ext import commands
from webserver import refresh

client = commands.Bot(command_prefix='!') 
client.remove_command('help')

@client.command(name = 'help')
async def help(context):
  help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

  help_embed.add_field(name = '!study [duration of study period] [duration of break] [number of cycles]', value = 'begin study session', inline = False)
  help_embed.add_field(name = '!study', value = 'Leave all field blank for recommened settings !study 30 5 4', inline = False) 
  help_embed.add_field(name = '!study [duration of study period] [duration of break]', value = 'Leave cycle field blank for infinite session', inline = False) 
  help_embed.add_field(name = '!quit', value = 'end current study session', inline = False) 
  help_embed.add_field(name = '!status', value = 'check timer of current study session', inline = False)

  await context.message.channel.send(embed = help_embed) 

@client.command(name='status')
async def status(context):
  global start
  try:
    timer_embed = discord.Embed(title = 'Timer', description = str(int(timer-(time.time()-start))//60) + ':' + str(int(round(((timer-(time.time()-start))%60), 0))) + ' minutes remaining', color = 0x831b6d)
  except:
    timer_embed = discord.Embed(title = 'Looks like a study session hasn\'t started yet.')
  await context.message.channel.send(embed = timer_embed)

@client.command(name='study')
async def study(context, *args):
  global start
  global isStudying
  global timer
  change = -1
  isStudying = True
  state = 1    
  start = time.time() 
  channel = context.message.channel

  try:

    if len(args) == 0:
      studyTime = 1800
      breakTime = 300
      cycles = 4
    elif len(args) == 2:
      studyTime = int(args[0]) * 60
      breakTime = int(args[1]) * 60    
      cycles = 1
      change = 0
    elif len(args) == 3:
      studyTime = int(args[0]) * 60
      breakTime = int(args[1]) * 60     
      cycles =  int(args[2]) * 2

    study_embed = discord.Embed(title = 'Study Time!', description = ('Current session: ' + str(int(studyTime/60)) + ':00' + ' min remaining'), color=0x831b6d)
    study_embed.set_footer(text = 'Type !status to check current timer')

    break_embed = discord.Embed(title = 'Break Time!', description = ('Current session: ' + str(int(breakTime/60)) + ':00' + ' min remaining'), color=0x831b6d)
    study_embed.set_footer(text = 'Type !status to check current timer')

    quit_embed = discord.Embed(title = 'Good session!', color=0x831b6d)

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
    await channel.send(embed = quit_embed)
  except Exception as e: 
    print(e)
    if start == ' ':
      await channel.send(embed = quit_embed)
    else:
      end_embed = discord.Embed(description = '!study [Duration of studying] [Duration of break] [Cycles]', color=0x831b6d)
      end_embed.set_footer(text = 'Leave all field blank for recommened settings !study 30 5 4 or leave cycles blank for an infinite session')
      await channel.send(embed = end_embed)

@client.command(name='quit')
async def quit(context):
  global isStudying
  global start
  start = ' '
  isStudying = False

@client.command(name = 'remind')
async def remind(context, *args):
  current = time.time()
  message = 'Reminder: '
  try:
    for i in args[1:]:
      message += (i + ' ')
    while (time.time() - current <= int(args[0])*60):
      await asyncio.sleep(1)
    print(message)
    msg_embed = discord.Embed(description = message, color=0x831b6d)
    await context.message.channel.send(embed = msg_embed)
  except Exception as e: 
    print(e)
    end_embed = discord.Embed(description = '!remind [Number of minutes to remind in] [Message to send]', color=0x831b6d)
    await context.message.channel.send(embed = end_embed)
  



@client.event
async def on_ready():
  print('Bot is online')

#refresh()
client.run(os.environ['token'])
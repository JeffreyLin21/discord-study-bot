import discord
from discord.ext import commands
import time
import asyncio

class Study(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(name = 'study')
  async def study(self, ctx):
    return

  @study.command(name='status')
  async def status(self, ctx):
    global start
    global timer
    try:
      timer_embed = discord.Embed(title = 'Timer', description = str(int(timer-(time.time()-start)/60)) + ':' + str(int(round((((timer * 60)-(time.time()-start))%60), 0))) + ' minutes remaining', color = 0x831b6d)
    except:
      timer_embed = discord.Embed(title = 'Looks like a study session hasn\'t started yet.')
    await ctx.author.send(embed = timer_embed)

  @study.command(name='start')
  async def start(self, ctx, studyTime = 30, breakTime = 5, cycles = 4):

    global start
    global isStudying
    global timer
    isStudying = True
    state = 1    
    start = time.time() 
    author = ctx.author

    try:

      study_embed = discord.Embed(title = 'Study Time!', description = ('Current session: ' + str(int(studyTime)) + ':00' + ' min remaining'), color=0x831b6d)
      study_embed.set_footer(text = 'Type !status to check current timer')

      break_embed = discord.Embed(title = 'Break Time!', description = ('Current session: ' + str(int(breakTime)) + ':00' + ' min remaining'), color=0x831b6d)
      study_embed.set_footer(text = 'Type /study status to check current timer')

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
        end_embed = discord.Embed(description = '/study [Duration of studying] [Duration of break] [Cycles]', color=0x831b6d)
        end_embed.set_footer(text = 'Leave all field blank for recommened settings !study 30 5 4 or leave cycles blank for an infinite session')
        await author.send(embed = end_embed)

  @study.command(name='quit')
  async def quit(self, ctx):
    global isStudying
    global start
    start = ' '
    isStudying = False

def setup(client):
  client.add_cog(Study(client))

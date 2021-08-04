import discord
from discord import message
from discord.ext import commands
from collections import deque
from cogs.database.discord_database import get, insert

user_study_list = {}

class Todo(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.group(name = 'todo')
  async def todo(self, ctx):
    return ctx

  @todo.command(name = 'add')
  async def add(ctx, *msg):
    global user_study_list
    try: 
      if (ctx.message.author in user_study_list):
        user_study_list[ctx.message.author].append(msg)
      else:
        user_study_list[ctx.message.author] = deque()
        user_study_list[ctx.message.author].append(msg)
      msg_embed = discord.Embed(description = "'" + msg + "'" + ' has been added to the todo list', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
    except Exception as e:
      print(e)
      msg_embed = discord.Embed(description = 'Please enter something to study', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
        
  @todo.command(name = 'next')
  async def add(self, ctx):
    try: 
      if (not user_study_list[ctx.message.author]):
        msg_embed = discord.Embed(description = 'There are no more topics to cover!', color=0x831b6d)
      else:
        user_study_list[ctx.message.author].popleft()
        msg_embed = discord.Embed(description = 'Next on the list: ' + user_study_list[ctx.message.author][0], color=0x831b6d)
        await ctx.message.author.send(embed = msg_embed)
    except Exception as e:
      print(e)
      msg_embed = discord.Embed(description = 'Hm... looks like something went wrong', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)

  @todo.command(name = 'clear')
  async def clear(self, ctx, limit = -1):
    try: 
      if limit == -1:
        user_study_list[ctx.message.author].clear()
      else:
        for i in range(0, limit):
          user_study_list[ctx.message.author].popleft()
      msg_embed = discord.Embed(description = 'Topics have been cleared!', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
    except Exception as e:
      print(e)
      msg_embed = discord.Embed(title = '!todo clear [number of topics to clear]', description = 'Leave last field blank to clear all', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)

  @todo.command(name = 'list')
  async def list(self, ctx):
    global user_study_list
    try: 
      msg = str(user_study_list[ctx.message.author])
      msg_embed = discord.Embed(description = msg[7: -2], color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
    except Exception as e:
      print(e)
      msg_embed = discord.Embed(description = 'Hm... looks like you don\'t have a list', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)

  @todo.command(name = 'save')
  async def save(self, ctx):
    try:
      msg = (str(user_study_list[ctx.message.author]))[7: -2]
      insert(ctx.message.author.id, 'study_list', msg)
      msg_embed = discord.Embed(description = 'List saved', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
    except Exception as e:
      print(e)
      msg_embed = discord.Embed(description = 'Hm... looks like you don\'t have a list', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)

  @todo.command(name = 'load')
  async def load(self, ctx):
    global user_study_list
    try:
      msg = get(ctx.message.author.id, 'study_list')[1:-1]
      list = msg.split(",")
      user_study_list[ctx.message.author] = deque()
      for i in list:
          user_study_list[ctx.message.author].append(i)
      msg_embed = discord.Embed(description = 'List has been loaded', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
    except Exception as e:
      print(e)
      msg_embed = discord.Embed(description = 'Hm... looks like you don\'t have a list', color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)

def setup(client):
  client.add_cog(Todo(client))

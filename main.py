import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/') 

@client.command(name='start')
async def start(ctx):
  msg_embed = discord.Embed(title = 'Hello I am Study Bot', description = "created by Jeffrey Lin", color = 0x831b6d)
  await ctx.message.author.send(embed = msg_embed)

@client.event
async def reload_extention(ctx, extention = ''):
  try:
    if (extention == ''):
      for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
          client.unload_extension(f'cogs.{filename[:-3]}')
          client.load_extension(f'cogs.{filename[:-3]}')
          print (f'Cog:\'{filename}\' was loaded')
    else:
      client.unload_extension(f'cogs.{extention}')
      client.load_extension(f'cogs.{extention}')
  except Exception as e:
    print (e)
    print ('Warning some cogs could not be loaded')   

@client.event
async def on_ready():
  print('Bot is online')

def load_bot():
  client.remove_command('help')
  try:
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print (f'Cog:\'{filename}\' was loaded')
    print ('All cogs loaded')
  except Exception as e:
    print (e)
    print ('Warning some cogs could not be loaded')
  token = open("token.txt", "r")
  client.run(token.read())

load_bot()


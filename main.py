import os
import discord
from cogs.database import init_database 
from discord.ext import commands

client = commands.Bot(command_prefix='/') 

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('Studying'))
  print('Bot is online')

"""" uncomment to check self id for verification
@client.command(name='check_self_id')
async def check_self_id(ctx):
  msg_embed = discord.Embed(title = 'Hello I am Study Bot', description = "Your id is: " + str(ctx.author.id), color = 0x831b6d)
  await ctx.message.author.send(embed = msg_embed)
"""
def verification(ctx):
  return ctx.author.id == 220287401833136129

@client.command()
@commands.check(verification)
async def reload_extension(ctx):
  try:

    if (ctx == ''):
      for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
          if filename == '__init__.py':
            continue
          client.unload_extension(f'cogs.{filename[:-3]}')
          client.load_extension(f'cogs.{filename[:-3]}')
          print (f'Cog:\'{filename}\' was reloaded')
      print ('All cogs were reloaded')

    else:
      client.unload_extension(f'cogs.{ctx}')
      client.load_extension(f'cogs.{ctx}')

  except Exception as e:
    print (e)
    print ('Warning some cogs could not be loaded')   

def load_bot():
  client.remove_command('help')

  try:
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        if filename == '__init__.py':
          continue
        client.load_extension(f'cogs.{filename[:-3]}')
        print (f'Cog:\'{filename}\' was loaded')
    print ('All cogs loaded')
    init_database.load_database()

  except Exception as e:
    print (e)
    print ('Warning some cogs could not be loaded')

  token = open("token.txt", "r")
  client.run(token.read())

load_bot()


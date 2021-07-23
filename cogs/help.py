import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(name = 'help')
  async def help(self, ctx):
    return

  # outdated
  @help.command(name = 'all')
  async def all(self, ctx):
    help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

    help_embed.add_field(name = '!study [duration of study period] [duration of break] [number of cycles]', value = 'begin study session', inline = False)
    help_embed.add_field(name = '!study', value = 'Leave all field blank for recommened settings !study 30 5 4', inline = False) 
    help_embed.add_field(name = '!study [duration of study period] [duration of break]', value = 'Leave cycle field blank for infinite session', inline = False) 
    help_embed.add_field(name = '!quit', value = 'end current study session', inline = False) 
    help_embed.add_field(name = '!status', value = 'check timer of current study session', inline = False)

    await ctx.message.author.send(embed = help_embed) 

  #@help.command(name = 'todo')
  #make a commands more detailed in subcommands with name that is the same as the command

def setup(client):
  client.add_cog(Help(client))



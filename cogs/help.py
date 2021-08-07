import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(name = 'help')
  async def help(self, ctx):
    help_embed = discord.Embed(title = 'List of valid commands', description = 'Use these general commands to view how to use the subcommands for each category', color = 0x831b6d)
    help_embed.add_field(name = '/help all', value = 'View all commands and subcommands', inline = False)
    help_embed.add_field(name = '/help remind', value = 'Commands related to the reminder feature', inline = False)
    help_embed.add_field(name = '/help study', value = 'Commands related to the study feature', inline = False)
    help_embed.add_field(name = '/help todo', value = 'Commands related to the todo list feature', inline = False)
    help_embed.add_field(name = '/help youtube', value = 'Commands related to the youtube search feature', inline = False)

    await ctx.message.author.send(embed = help_embed) 

  @help.command(name = 'all')
  async def all(self, ctx):
    help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

    help_embed.add_field(name = '/remind add [timer in minutes] [message to send]', value = 'Adds a new reminder', inline = False)
    help_embed.add_field(name = '/remind list', value = 'Lists all currently active reminders', inline = False)
    help_embed.add_field(name = '/remind clear [# of reminder to clear, use /remind list to check each reminder #]', value = 'Clears the selected reminder, leave blank to clear all', inline = False)

    help_embed.add_field(name = '/study start [duration of study in minutes] [duration of break in minutes] [number of cycles]', value = 'Starts a study session, leave any values blank to use default values (30, 5, 4).', inline = False)
    help_embed.add_field(name = '/study status', value = 'View the time left in current session', inline = False)
    help_embed.add_field(name = '/study quit', value = 'End the current study session', inline = False)

    help_embed.add_field(name = '/todo add [message to add to todo list]', value = 'Adds an item to the todo list', inline = False)
    help_embed.add_field(name = '/todo next', value = 'Removes the first item on the todo list on moves to the next item', inline = False)
    help_embed.add_field(name = '/todo clear [number of items to remove]', value = 'Removes the chosen number of items from the todo list starting from the top', inline = False)
    help_embed.add_field(name = '/todo list', value = 'Lists all the current items on the todo list', inline = False)
    help_embed.add_field(name = '/todo save', value = 'Saves the current todo list linked  to the current discord account', inline = False)
    help_embed.add_field(name = '/todo load', value = 'Loads a previous todo list linked to the current discord account', inline = False)

    help_embed.add_field(name = '/youtube search [search term]', value = 'Searches the given search term on YouTube and grabs the top 5 results', inline = False)
    help_embed.add_field(name = '/youtube searchc [search term]', value = 'Searches the given search term on YouTube and grabs the top 5 results in a compact format', inline = False)
    help_embed.add_field(name = '/youtube searchone [search term]', value = 'Searches the given search term on YouTube and grabs the top result', inline = False)

    await ctx.message.author.send(embed = help_embed) 

  @help.command(name = 'remind')
  async def remind(self, ctx):
    help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

    help_embed.add_field(name = '/remind add [timer in minutes] [message to send]', value = 'Adds a new reminder', inline = False)
    help_embed.add_field(name = '/remind list', value = 'Lists all currently active reminders', inline = False)
    help_embed.add_field(name = '/remind clear [# of reminder to clear, use /remind list to check each reminder #]', value = 'Clears the selected reminder, leave blank to clear all', inline = False)

    await ctx.message.author.send(embed = help_embed) 

  @help.command(name = 'study')
  async def study(self, ctx):
    help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

    help_embed.add_field(name = '/study start [duration of study in minutes] [duration of break in minutes] [number of cycles]', value = 'Starts a study session, leave any values blank to use default values (30, 5, 4).', inline = False)
    help_embed.add_field(name = '/study status', value = 'View the time left in current session', inline = False)
    help_embed.add_field(name = '/study quit', value = 'End the current study session', inline = False)

    await ctx.message.author.send(embed = help_embed) 

  @help.command(name = 'todo')
  async def todo(self, ctx):
    help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

    help_embed.add_field(name = '/todo add [message to add to todo list]', value = 'Adds an item to the todo list', inline = False)
    help_embed.add_field(name = '/todo next', value = 'Removes the first item on the todo list on moves to the next item', inline = False)
    help_embed.add_field(name = '/todo clear [number of items to remove]', value = 'Removes the chosen number of items from the todo list starting from the top', inline = False)
    help_embed.add_field(name = '/todo list', value = 'Lists all the current items on the todo list', inline = False)
    help_embed.add_field(name = '/todo save', value = 'Saves the current todo list linked  to the current discord account', inline = False)
    help_embed.add_field(name = '/todo load', value = 'Loads a previous todo list linked to the current discord account', inline = False)

    await ctx.message.author.send(embed = help_embed) 

  @help.command(name = 'youtube')
  async def youtube(self, ctx):
    help_embed = discord.Embed(title = 'Help', description = 'List of valid commands', color = 0x831b6d)

    help_embed.add_field(name = '/youtube search [search term]', value = 'Searches the given search term on YouTube and grabs the top 5 results', inline = False)
    help_embed.add_field(name = '/youtube searchc [search term]', value = 'Searches the given search term on YouTube and grabs the top 5 results in a compact format', inline = False)
    help_embed.add_field(name = '/youtube searchone [search term]', value = 'Searches the given search term on YouTube and grabs the top result', inline = False)

    await ctx.message.author.send(embed = help_embed) 

def setup(client):
  client.add_cog(Help(client))



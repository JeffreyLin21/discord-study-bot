import discord
from discord.ext import commands
import time
import asyncio

class Reminder(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(name = 'reminder')
  async def reminder(self, ctx):
    return

  @reminder.command(name = 'set')
  async def set(self, ctx, remind_time = 1, message = 'not sure why, but you created this reminder!'):
    current = time.time()
    reminder = 'Reminder: ' + message
    try:
      while (time.time() - current <= remind_time * 60):
        await asyncio.sleep(1)
      msg_embed = discord.Embed(description = message, color=0x831b6d)
      await ctx.message.author.send(embed = msg_embed)
    except Exception as e: 
      print(e)
      end_embed = discord.Embed(description = '!remind [Number of minutes to remind in] [Message to send]', color=0x831b6d)
      await ctx.message.author.send(embed = end_embed)

  #@reminder.command(name = 'list')
  #@reminder.command(name = 'clear')

def setup(client):
  client.add_cog(Reminder(client))

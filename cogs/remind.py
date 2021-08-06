import discord
from discord.ext import commands
import time
import asyncio

user_reminder_list = {}

class Remind(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(name = 'remind')
  async def remind(self, ctx):
    return ctx

  @remind.command(name = 'add')
  async def add(self, ctx, remind_time = 1, *message):
    current = time.time()

    msg = ' '.join(message)

    if msg == '':
      msg = 'Not sure why, but you created this reminder!'

    reminder = 'Reminder: ' + msg

    user_reminder_list[reminder] = [remind_time, time.time()]

    msg_embed = discord.Embed(description = 'Reminder has been created!', color=0x831b6d)
    await ctx.author.send(embed = msg_embed)

    try:
      while (time.time() - current <= remind_time * 60):
        await asyncio.sleep(1)
      user_reminder_list.pop(reminder)
      msg_embed = discord.Embed(description = reminder, color=0x831b6d)
      await ctx.author.send(embed = msg_embed)
    except Exception as e: 
      print(e)
      end_embed = discord.Embed(description = '!remind [Number of minutes to remind in] [Message to send]', color=0x831b6d)
      await ctx.author.send(embed = end_embed)

  @remind.command(name = 'list')
  async def list(self, ctx):
    global user_reminder_list
    try:
      msg_embed = discord.Embed(title = 'List of active reminders', description = "Use '/reminder clear [reminder number]' to remove a reminder", color=0x831b6d)
      num = 1

      for i in user_reminder_list:
        msg_embed.add_field(name =  str(num) + ': ' + i[10:], value = str(int(user_reminder_list[i][0]-(time.time()-user_reminder_list[i][1])/60)) + ':' + str(int(round((((user_reminder_list[i][0] * 60)-(time.time()-user_reminder_list[i][1]))%60), 0))) + ' minutes remaining', inline = False)
        num += 1

      if not user_reminder_list:
        msg_embed.add_field(name =  'No active reminders', value = "Use '/remind add [timer] [message]' to add a new reminder", inline = False)

      await ctx.author.send(embed = msg_embed)
    except Exception as e: 
      print(e)
      end_embed = discord.Embed(description = 'Check command paramters and try again', color=0x831b6d)
      await ctx.author.send(embed = end_embed)

      
  @remind.command(name = 'clear')
  async def clear(self, ctx, target = 0):
    global user_reminder_list

    if target == 0:
      user_reminder_list.clear()

    else:

      j = 1
      for i in user_reminder_list:
        if j == target:
          user_reminder_list.pop(i)
          break
        j += 1
    msg_embed = discord.Embed(description = 'Reminder(s) have been cleared', color=0x831b6d)
    await ctx.author.send(embed = msg_embed)    

def setup(client):
  client.add_cog(Remind(client))

from http.client import responses
import json
import discord
from discord.ext import commands

from googleapiclient.discovery import build

class Youtube(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    global youtube 

    api_key = (open("api.txt", "r")).read()
    youtube = build('youtube', 'v3', developerKey = api_key)

  @commands.group(name = 'youtube')
  async def youtube(self, ctx):
    return ctx

  @youtube.command(name = 'search')
  async def search(self, ctx, *search_term):
    global youtube

    query = ' '.join(search_term)

    request = youtube.search().list(part = 'snippet', q = query, type = 'video')
    response = request.execute()

    for i in response['items']:
      url = 'https://www.youtube.com/watch?v=' + i['id']['videoId']
      await ctx.author.send(url)

  @youtube.command(name = 'searchc')
  async def searchc(self, ctx, *search_term):
    global youtube

    query = ' '.join(search_term)

    request = youtube.search().list(part = 'snippet', q = query, type = 'video')
    response = request.execute()

    msg_embed = discord.Embed(title = 'YouTube search results:', description ='Source: [YouTube](https://www.youtube.com)', color=0x831b6d)

    for i in response['items']:
      url = 'https://www.youtube.com/watch?v=' + i['id']['videoId']
      msg_embed.add_field(name = i['snippet']['title'], value = f'[{url}]({url})', inline = False)
      
    await ctx.author.send(embed = msg_embed)

  @youtube.command(name = 'searchone')
  async def searchone(self, ctx, *search_term):
    global youtube

    query = ' '.join(search_term)

    request = youtube.search().list(part = 'snippet', q = query, type = 'video', maxResults = 1)
    response = request.execute()

    for i in response['items']:
      url = 'https://www.youtube.com/watch?v=' + i['id']['videoId']
      await ctx.author.send(url)

def setup(client):
  client.add_cog(Youtube(client))
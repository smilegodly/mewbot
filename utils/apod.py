import requests
import discord
from discord.ext import commands
from discord import Game
import asyncio
import json
import urllib.request
import io
import aiohttp

class Apod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	def getApodData():
		apod = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

		with urllib.request.urlopen(apod) as response:
			data = json.loads(response.read().decode())

		return data

'''
	async def createBytesInstance(my_url):
		async with aiohttp.ClientSession() as session:
			async with session.get(my_url) as resp:
				if resp.status != 200:
					return await channel.send('Could not download file...')
				data = io.BytesIO(await resp.read()) #create BytesIO instance
				return data
'''
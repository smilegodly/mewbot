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

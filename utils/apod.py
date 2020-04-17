import requests
import discord
from discord.ext import commands
from discord import Game
import asyncio

class Apod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	apod = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

#Author smilegodly
import requests
import subprocess
import discord
from discord.ext import commands
from discord import Game
import asyncio
from datetime import datetime
import youtube_dl
from utils.funcs import Funcs
from utils.ytplayer import Music
from utils.secretgrabber import getSecret

PREFIX = ("!", "?", "./", "~")

bot = commands.Bot(command_prefix=PREFIX)

bot.remove_command('help')

secret = getSecret()

@bot.event
async def on_ready():
	game = discord.Game("RuneLite")
	await bot.change_presence(status=discord.Status.idle, activity=game)
	print("Logged in as ")
	print(bot.user.name)
	print(bot.user.id)
	print("-------------")

bot.add_cog(Music(bot))
bot.add_cog(Funcs(bot))
bot.run(secret)

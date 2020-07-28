import requests
import subprocess
import discord
from discord.ext import commands
from discord import Game
import asyncio
from datetime import datetime
from howdoi import howdoi

class Funcs(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self,ctx):
		author = ctx.message.author
		
		embed = discord.Embed(
			color = discord.Colour.green()
		)

		embed.set_author(name='Commands')

		embed.add_field(name='help', value='Shows Information For commands',inline=False)
		embed.add_field(name='howdoi', value='Instant coding answers',inline=False)
		embed.add_field(name='square', value='Squares a number',inline=False)
		embed.add_field(name='hello', value='Says hello',inline=False)
		embed.add_field(name='bitcoin', value='Gets Information on bitcoin',inline=False)
		embed.add_field(name='item', value='Gets Information on OSRS items',inline=False)

		await ctx.author.send(embed=embed)

	@commands.command()
	async def howdoi(self,ctx,question):#sanitize the **** out of the user input (question)
			
		# Get howdoi answer 
		query = question
		parser = howdoi.get_parser()
		args = vars(parser.parse_args(query.split(' ')))
		output = howdoi.howdoi(args)
		await ctx.send("```" + "\n" + output + "\n" + "```")
		
		# Get stackoverflow Link to that answer
		linkCommand = '-l'
		query = linkCommand + ' ' + question
		parser = howdoi.get_parser()
		args = vars(parser.parse_args(query.split(' ')))
		output = howdoi.howdoi(args)
		await ctx.send("\n" + output + "\n")
		return

	@commands.command()
	async def square(self,ctx,num):
		sq_val = int(num) * int(num)
		await ctx.send(str(num) + " squared is " + str(sq_val))

	@commands.command(description="greets a user",
		aliases=['hey', 'hi', 'yo', 'ay', 'sup', 'wassup'],
		pass_context=True)
	async def hello(self,ctx):
		await ctx.send("Good day , " + ctx.message.author.mention)

	@commands.command()
	async def bitcoin(self,ctx):
		url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
		response = requests.get(url)
		value = response.json()['bpi']['USD']['rate']
		country_code = response.json()['bpi']['USD']['code']
		await ctx.send("Bitcoin price is $" + value + " " + country_code)

	@commands.command()
	async def item(self,ctx,itemName):
		returnMsg = "Item not found."
		url = 'https://rsbuddy.com/exchange/summary.json'
		response = requests.get(url).json()
		for id, item in response.items():
			if  item['name'].lower() == itemName.lower():
				buy_avg = item['buy_average']
				sell_avg = item['sell_average']
				num_bought = item['buy_quantity']
				num_sold = item['sell_quantity']
				returnMsg = "Buy average : {}\r\nSell average : {}\r\nNumber bought : {}\r\nNumber sold : {}"
				await ctx.send(returnMsg.format(buy_avg, sell_avg, num_bought, num_sold))
				return
		await ctx.send("Item not found")

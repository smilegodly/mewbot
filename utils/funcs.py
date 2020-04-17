import requests
import subprocess
import discord
from discord.ext import commands
from discord import Game
import asyncio
from datetime import datetime

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
	async def howdoi(self,ctx,question):
		# Get howdoi answer 
		command = 'howdoi'
		cmd = [command, question]
		subprocess.run(cmd)
		check = command + ' ' + question
		output = subprocess.check_output(check, shell=True, universal_newlines=True)
		await ctx.send("```" + "\n" + output + "\n" + "```")
		
		# Get stackoverflow Link to that answer
		linkCommand = '-l'
		linkCmd = [command, linkCommand, question]
		subprocess.run(linkCmd)
		linkCheck = command + ' ' + linkCommand + ' ' + question
		linkOutput = subprocess.check_output(linkCheck, shell=True, universal_newlines=True)
		await ctx.send("\n" + linkOutput + "\n")
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

#BELOW CODE IS UNDER CONSTRUCTION :)
'''
	#job times
	battlestaves_time='20:00' #time is in 24hr format
	bowl_time='16:20' #time is in 24hr format
	warning_for_420='16:18' #time is in 24hr format
	bowl_time_morning='04:20' #time is in 24hr format
	warning_for_420_morning='04:18' #time is in 24hr format

	#assigning ID's
	osrs_message_channel_id=367061561405341697 #channel ID
	stoner_shit_channel_id=207637066467508225 
	commands_shit_channel_id=518253505669103617
	bowl_time_role = '<@&585239417569148931>'	#role ID
	goobId = '<@255739523764453390>'			#user ID

	#getting channels
	osrs_message_channel=commands.get_channel(osrs_message_channel_id)
	stoner_shit_channel=commands.get_channel(stoner_shit_channel_id)
	commands_shit_channel=commands.get_channel(commands_shit_channel_id)

	async def time_check():
		await commands.wait_until_ready()
		while not commands.is_closed:
			now=datetime.strftime(datetime.now(),'%H:%M')
			if now == battlestaves_time:
				await commands.send_message(osrs_message_channel, 'You have battlestaves waiting to be collected from Zaff... %s ' % goobId)
				time=90
			elif now == warning_for_420 or now == warning_for_420_morning:
				await commands.send_message(stoner_shit_channel, 'Hey, It''s 4:18... %s ' % bowl_time_role)
				time=90
			elif now == bowl_time or now == bowl_time_morning:
				await commands.send_message(stoner_shit_channel, 'It is Bowl Time... %s ' % bowl_time_role)
				time=90
			else:
				time=1
			await asyncio.sleep(time)
'''

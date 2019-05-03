import asyncio
import requests
import discord
import json
import time
from discord.ext import commands


URL = "https://linode.ghazlawl.com/ark/mods/auctionhouse/api/json/v1/auctions/"


#KEY = ""
#ServerBase = "https://ark-servers.net/api/?object=servers&element=detail&key={}"
#Server = ServerBase.format(KEY)

bot = commands.Bot(activity=discord.Game("Ark: Auction House Mod") ,command_prefix='ah!')

@bot.command(pass_context=True)
async def online(ctx):
	await ctx.send("This feature is currently unavaliable. please wait for a few days till we can fix this")
	await asyncio.sleep(3)

@bot.command(pass_context=True)
async def getListing(ctx, Name1):
	global URL
	Global = requests.get(url = URL)
	GlobalData = json.loads(Global.content)
	x = 0
	for item in GlobalData["Auctions"]:
		if item["Name"] == Name1:
			x = x + 1
			if x == 20:
				break
			await ctx.send("Cost: " + item["AskingClass"])
			await ctx.send("Cost AMT : " + str(item["AskingAmount"]))
			await ctx.send("Selling AMT: " + str(item["Quantity"]))
			await ctx.send("Seller : " + item["Seller"]["Name"])
			await ctx.send("New Person")
			await asyncio.sleep(3)
@bot.command(pass_context=True)
async def botHelp(ctx):
	await ctx.send("Discord Auction House Bot made By: Bennyturtle")
	await ctx.send("Commands:")
	await ctx.send("getListing (Item Name):: Gets all the listings for that item type")
	await ctx.send("WARNING: getListing gets every listing from every server, so please dont use it in public chat")
	await ctx.send("online :: displays the status of the servers")
	await ctx.send("botHelp :: displays this help page")
	await asyncio.sleep(3)

bot.run('')






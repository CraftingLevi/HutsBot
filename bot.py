# bot.py

import discord
from thema_tools import thema_sheet
import pandas as pd 
from discord.ext import commands
import asyncio
import numpy as np
import re
import json
import os

with open(os.path.join('src', 'config.JSON'), 'r') as file:
	config = json.load(file)
	TOKEN = config['token']
	accepted_authors = config['thema_users']


bot = commands.Bot(command_prefix='?')
global current_theme
@bot.command(pass_context=True)
async def hello(ctx):
	msg = f'Hello {ctx.message.author.mention}'
	await ctx.message.channel.send(msg)

@bot.command(pass_context=True)
async def bonjour(ctx):
	msg = f'Bonjour Monsieur {ctx.message.author.mention}'
	await ctx.message.channel.send(msg)

@bot.command(pass_context=True)
async def welterusten(ctx):
	msg = f'Welterusten Meneer {ctx.message.author.mention}!\n Slaap zacht :michiel2:'
	await ctx.message.channel.send(msg)
	author = ctx.message.author
	print(author.id)
	channel = author.voice.channel
	print(f"---- Joining {channel}-----")
	vc = await channel.connect()
	audio_source = discord.FFmpegPCMAudio(os.path.join('src', 'welterusten.mp3'))
	vc.play(audio_source, after=lambda: print('done'))
	while vc.is_playing():
		await asyncio.sleep(1)
	# disconnect after the player has finished
	vc.stop()
	await vc.disconnect()

@bot.command(pass_context=True)
async def stop(ctx):
	vc = ctx.bot.voice_clients[0]
	vc.stop()
	await vc.disconnect()

@bot.command(pass_context=True)
async def fortuin(ctx, *numb):
	numbs = [int(re.sub(r"[^0-9]", "", i.strip())) for i in numb]
	max_numb = max(numbs)
	min_numb = min(numbs)
	author = ctx.message.author
	print(author.id)
	channel = author.voice.channel
	print(f"---- Joining {channel}-----")
	await ctx.message.channel.send(f"{ctx.message.author.mention} draait het rad met getallen tussen {min_numb} & {max_numb}")
	try:
		vc = await channel.connect()
	except:
		print('already connected...')
	audio_source = discord.FFmpegPCMAudio(os.path.join('src', 'themaselectie.mp3'))
	vc.play(audio_source, after=lambda: print('done'))
	while vc.is_playing():
		await asyncio.sleep(1)
	# disconnect after the player has finished
	vc.stop()
	await ctx.message.channel.send(f"{ctx.message.author.mention} heeft {np.random.randint(low=min_numb, high=max_numb)} gedraaid!")
	await vc.disconnect()

@bot.command(pass_context=True)
async def thema(ctx):
	author = ctx.message.author
	if author.id in accepted_authors:
		channel = author.voice.channel
		print(f"---- Joining {channel}-----")
		await ctx.message.channel.send("Het moment is daar! Een thema zal worden gekozen!")
		try:
			vc = await channel.connect()
		except:
			print('already connected...')
		audio_source = discord.FFmpegPCMAudio(os.path.join('src', 'themaselectie.mp3'))
		vc.play(audio_source, after=lambda: print('done'))
		while vc.is_playing():
			await asyncio.sleep(1)
		# disconnect after the player has finished
		current_theme = thema_sheet()
		await ctx.message.channel.send(current_theme.drawn_thema_to_string())
		vc.stop()
		await vc.disconnect()
	else:
		await ctx.message.channel.send(f"Helaas, {ctx.message.author.mention} je mag geen themas rollen :/")



@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

bot.run(TOKEN)
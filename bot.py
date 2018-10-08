import discord
import os
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def teams(ctx):
    players = []
    team1 = []
    team2 = []
    
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.VoiceChannel):
            players += channel.members
            
    for player in players:
        if random.random() < 0.5:
            team1 += player
        else:
            team2 += player
            
    while abs(len(team1) - len(team2)) > 1:
        if len(team1) > len(team2):
            team1.pop()
            team2.push()
        else:
            team2.pop()
            team1.push()
            
    message = "Team 1: "
    for player in team1:
        message += player.display_name
        message += ", "
        
    message = message[:-2]
    message += "\n"
    message += "Team 2: "
    for player in team2:
        message += player.display_name
        message += ", "
    message = message[:-2]
        
    await ctx.send(message)
    
bot.run(os.environ['BOT_TOKEN'])

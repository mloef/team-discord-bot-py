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
async def teams(ctx, channelID=None):
    players, team1, team2 = [], [], []
    
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.VoiceChannel):
            players += channel.members
            
    for player in players:
        if random.random() < 0.5:
            team1.append(player.display_name)
        else:
            team2.append(player.display_name)
            
    while abs(len(team1) - len(team2)) > 1: #balance teams
        if len(team1) > len(team2):
            team2.append(team1.pop())
        else:
            team1.append(team2.pop())
            
    message = "Team 1: "
    message += ", ".join(team1)
    
    message += "\nTeam 2: "
    message += ", ".join(team2)
        
    await ctx.send(message)
    
bot.run(os.environ['BOT_TOKEN'])

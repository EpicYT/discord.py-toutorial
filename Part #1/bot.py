import discord
from discord.ext import commands
bot=commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print('Bot is online')

@bot.command()
async def p(ctx):
    await ctx.send('Hello')
bot.run('ODg0MTA1Mjc4OTM5ODg1NjM4.YTTpNA.SXthKv5NaM3x6wdSvEkpAKxgI-Y')
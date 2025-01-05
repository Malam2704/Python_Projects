from discord.ext import commands
import discord

BOT_TOKEN = 'MTMyNTUxMTI5MDgwMTg4MTA5OA.GUQQ76.niUfDeeYkhe_7CkvQFQvuPhS50Bt4_AZpJcHU0'
Channel_ID = 1325513357935120384

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Study Bot")

bot.run(BOT_TOKEN)
from discord.ext import commands
import discord



bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Study Bot")

bot.run(BOT_TOKEN)
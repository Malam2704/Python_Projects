import discord
from discord.ext import commands

# You can change the prefix to anything you like, e.g., "?" or "!!"
intents = discord.Intents.default()
intents.message_content = True  # Needed for reading message content in some forks
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command()
async def hello(ctx):
    """
    A simple command that the bot responds to when someone types !hello
    """
    await ctx.send("Hello there! I am alive.")

# IMPORTANT: Replace 'YOUR_BOT_TOKEN_HERE' with the actual token you copied from the Developer Portal
bot.run("")

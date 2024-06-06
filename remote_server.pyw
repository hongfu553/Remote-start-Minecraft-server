import discord
from discord.ext import commands
import subprocess
import os
import sys
import atexit

lock_file_path = "script.lock"

if os.path.exists(lock_file_path):
    print("Script is already running.")
    sys.exit()

with open(lock_file_path, "w") as lock_file:
    lock_file.write(str(os.getpid()))

def remove_lock_file():
    if os.path.exists(lock_file_path):
        os.remove(lock_file_path)

atexit.register(remove_lock_file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "%", intents = intents)

# 替換成剛剛創建的Discord bot token
key = "your discord bot token"

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

@bot.command()
async def server_start(ctx):
    try:
        shortcut_file_path = "run.bat.lnk"
        await ctx.send("伺服器啟動中(約1~2分鐘)...")
        subprocess.run(["cmd", "/c", shortcut_file_path], check=True)
        await ctx.send("伺服器已關閉!")
    except Exception as e:
        await ctx.send(f"啟動伺服器時出錯: {e}")

bot.run(key)

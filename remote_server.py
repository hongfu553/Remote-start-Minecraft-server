import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

key = os.getenv('DC_key')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

@bot.command()
async def server_start(ctx):
    try:
        # 替換 'path_to_your_bat_file.bat' 為你真正的 .bat 文件的路徑
        bat_file_path = "path_to_your_bat_file.bat"
        subprocess.run([bat_file_path], check=True)
        await ctx.send("伺服器已啟動！")
    except Exception as e:
        await ctx.send(f"啟動伺服器時出錯: {e}")

bot.run(key)
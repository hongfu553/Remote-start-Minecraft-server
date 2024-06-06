import discord
from discord.ext import commands
import subprocess

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)

# 替換成剛剛創建的Discord bot token
key = ('DC_token_key')

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
        subprocess.Popen(["cmd", "/c", shortcut_file_path])
    except Exception as e:
        await ctx.send(f"啟動伺服器時出錯: {e}")

bot.run(key)
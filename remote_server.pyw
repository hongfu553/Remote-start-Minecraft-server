import discord
from discord.ext import commands
import subprocess
from dotenv import load_dotenv
import os
import psutil
import time
import requests

def mcstatus():
    response = requests.get("https://api.ipify.org?format=json")
    response.raise_for_status()
    public_ip = response.json()['ip']
    
    status = "https://api.mcsrvstat.us/3/" + public_ip
    mc_server_status_response = requests.get(status)
    mc_server_status_response.raise_for_status()
        
    mc_server_status = mc_server_status_response.json()
    server_online = mc_server_status.get("online", False)
    return server_online

load_dotenv()
key =os.getenv("key")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="%", intents=intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def TM(ctx):
    cpu = psutil.cpu_percent(interval=5)

    memory = psutil.virtual_memory()

    initial_net_info = psutil.net_io_counters()
    initial_bytes_sent = initial_net_info.bytes_sent
    initial_bytes_recv = initial_net_info.bytes_recv

    time.sleep(1)

    current_net_info = psutil.net_io_counters()
    current_bytes_sent = current_net_info.bytes_sent
    current_bytes_recv = current_net_info.bytes_recv

    send_kbps = (current_bytes_sent - initial_bytes_sent) * 8 / 1000
    recv_kbps = (current_bytes_recv - initial_bytes_recv) * 8 / 1000

    computer = [
        f"CPU使用率: {cpu:.2f}%",
        f"內存已使用: {memory.used / (1024 ** 3):.2f}/{memory.total / (1024 ** 3):.2f} GB",
        f"上傳數據量: {send_kbps:.2f} kbps",
        f"下載數據量: {recv_kbps:.2f} kbps",
        f"以上數據僅供參考"
    ]

    for info in computer:
        await ctx.send(info)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

@bot.command()
async def server_start(ctx):
    try:
        lnk_file = "run.lnk"
        await ctx.send("伺服器啟動中(約1~2分鐘)...")
        subprocess.Popen(["cmd", "/c", "start", lnk_file])
        
        timeout = time.time() + 300  # 5分鐘超時
        while True:
            if time.time() > timeout:
                await ctx.send("伺服器啟動超時。")
                break
            data = mcstatus()
            if data:
                await ctx.send("Minecraft server已啟動")
                break
            time.sleep(10)

    except subprocess.SubprocessError as e:
        await ctx.send(f"啟動伺服器時出錯: {e}")
    except Exception as e:
        await ctx.send(f"發生錯誤: {e}")

bot.run(key)
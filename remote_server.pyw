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
    response.raise_for_status()  # Check if the request was successful
    public_ip = response.json()['ip']
    
    status = "https://api.mcsrvstat.us/3/" + public_ip
    mc_server_status_response = requests.get(status)
    mc_server_status_response.raise_for_status()  # Check if the request was successful
        
    mc_server_status = mc_server_status_response.json()
    server_online = mc_server_status["online"]
    return server_online

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)

# 替換成剛剛創建的Discord bot token
key = os.getenv('DC_key')
host = os.getenv('host')

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def TM(ctx):
    # 使用1秒间隔采样CPU使用率
    cpu = psutil.cpu_percent(interval=5)

    memory = psutil.virtual_memory()
    net = psutil.net_io_counters()

    # 获取当前时间的网络IO数据
    initial_net_info = psutil.net_io_counters()
    initial_bytes_sent = initial_net_info.bytes_sent
    initial_bytes_recv = initial_net_info.bytes_recv

    # 等待1秒钟
    time.sleep(1)

    # 再次获取网络IO数据
    current_net_info = psutil.net_io_counters()
    current_bytes_sent = current_net_info.bytes_sent
    current_bytes_recv = current_net_info.bytes_recv

    # 计算1秒内发送和接收的数据量，并转换为kbps
    send_kbps = (current_bytes_sent - initial_bytes_sent) * 8 / 1024000
    recv_kbps = (current_bytes_recv - initial_bytes_recv) * 8 / 1024000

    computer = [
        f"CPU使用率: {cpu:.2f}%",
        f"內存已使用: {memory.used / (1024 ** 3):.2f}/{memory.total / (1024 ** 3):.2f} GB",
        f"上傳數據量: {send_kbps:.2f} Mbps",
        f"下載數據量: {recv_kbps:.2f} Mbps",
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
        
        while True:
            data = mcstatus()
            if data is False:
                time.sleep(10)
            elif data is True:
                await ctx.send("Minecraft server已啟動")
                break

    except Exception as e:
        await ctx.send(f"啟動伺服器時出錯: {e}")

bot.run(key)
import discord
from discord.ext import commands
import subprocess
import os
import sys
import atexit
import psutil

# 定义锁文件的路径
lock_file_path = "script.lock"

def is_running(pid):
    """检查给定的PID是否正在运行"""
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True

# 检查锁文件是否存在并且包含的PID是否对应一个正在运行的进程
if os.path.exists(lock_file_path):
    with open(lock_file_path, "r") as lock_file:
        try:
            existing_pid = int(lock_file.read().strip())
            if is_running(existing_pid):
                print("Script is already running.")
                sys.exit()
            else:
                print("Found a stale lock file. Removing it.")
                os.remove(lock_file_path)
        except ValueError:
            # 如果锁文件内容无法解析为整数，假定锁文件无效
            print("Found an invalid lock file. Removing it.")
            os.remove(lock_file_path)

# 创建锁文件
with open(lock_file_path, "w") as lock_file:
    lock_file.write(str(os.getpid()))

# 定义删除锁文件的函数
def remove_lock_file():
    if os.path.exists(lock_file_path):
        os.remove(lock_file_path)

# 注册在脚本退出时删除锁文件的函数
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

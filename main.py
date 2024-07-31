import discord
from discord.ext import commands
import datetime
import sqlite3
import subprocess
import os
import asyncio
import random
import collections

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

TOKEN = os.getenv('DISCORD_TOKEN')

# Constants
ALLOWED_CHANNEL_ID = 1264975987934761121
ALLOWED_GUILD_ID = 1264973683877744798
TEMP_ROLE_ID = 1264997863079940170
ROLE_ID = 1264975463672057907
SPECIAL_ROLE_ID = 1265025672225493223
LOG_CHANNEL_ID = 1266421667849043978
INVALID_NUMBERS = ['113', '911', '114', '115', '84357156328', '0357156328']
VIP_CHANNEL_ID = 1268130522731905079
VIP_ROLE_ID = 1268131048575729665

# Database setup
try:
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            expiration_time TEXT
        )
    ''')
    connection.commit()
except sqlite3.Error as e:
    print(f"Lỗi kết nối cơ sở dữ liệu: {e}")

# State storage
processes = []
recent_gifs = collections.deque(maxlen=4)
GIF_URLS = [
    "https://c.tenor.com/LmJ_S8wzHlkAAAAd/tenor.gif",
    "https://c.tenor.com/_zPDmll9gtYAAAAC/tenor.gif",
    "https://c.tenor.com/5eOY_XtahDoAAAAC/tenor.gif",
    "https://c.tenor.com/btBDlEIT5xUAAAAd/tenor.gif",
    "https://c.tenor.com/I-vY-Iq3zggAAAAC/tenor.gif",
    "https://c.tenor.com/zb0UToCgW9gAAAAC/tenor.gif",
    "https://c.tenor.com/XJS7LmGwm5QAAAAC/tenor.gif",
    "https://c.tenor.com/EqJh0gyBX5wAAAAd/tenor.gif",
    "https://c.tenor.com/wkz3IcpxCEUAAAAd/tenor.gif",
    "https://c.tenor.com/s73hsxgU3IAAAAAd/tenor.gif",
    "https://c.tenor.com/7plyfBPAR3AAAAAd/tenor.gif",
    "https://c.tenor.com/ejdvSGj5kCYAAAAC/tenor.gif",
    "https://c.tenor.com/xD5CN6oj8ysAAAAC/tenor.gif",
    "https://c.tenor.com/6Myx4MF6DjIAAAAC/tenor.gif",
    "https://c.tenor.com/2BmAiarixGAAAAAC/tenor.gif",
    "https://c.tenor.com/1nwkeOg8j48AAAAd/tenor.gif",
    "https://c.tenor.com/5wn9MtW_PYUAAAAd/tenor.gif",
    "https://c.tenor.com/L6bKFEaUkp0AAAAC/tenor.gif"
]

def TimeStamp():
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=7)).strftime('%Y-%m-%d %I:%M:%S %p')

def get_random_gif_url():
    available_gifs = [url for url in GIF_URLS if url not in recent_gifs]
    if not available_gifs:
        available_gifs = GIF_URLS
        recent_gifs.clear()
    chosen_gif = random.choice(available_gifs)
    recent_gifs.append(chosen_gif)
    return chosen_gif

async def log_to_channel(username, user_id, phone_number, execution_time):
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        log_message = f"{username} ||{user_id}|| {phone_number} - {execution_time}\n"
        await channel.send(log_message)

async def log_to_channel_vip(username, user_id, phone_number, execution_time):
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        log_message = f"**VIP** {username} ||{user_id}|| {phone_number} - {execution_time}\n"
        await channel.send(log_message)

def has_excluded_role(member):
    return discord.utils.get(member.guild.roles, id=1264997863079940170) in member.roles

@bot.event
async def on_ready():
    print(f'Kết nối thành công với {bot.user.name}')

def has_required_role(member):
    return discord.utils.get(member.guild.roles, id=ROLE_ID) in member.roles

async def add_and_remove_role(member):
    temp_role = discord.utils.get(member.guild.roles, id=TEMP_ROLE_ID)
    if temp_role:
        await member.add_roles(temp_role)
        await asyncio.sleep(120)
        await member.remove_roles(temp_role)
        channel = bot.get_channel(ALLOWED_CHANNEL_ID)
        if channel:
            ping_message = await channel.send(f'{member.mention}')
            await asyncio.sleep(1)
            await ping_message.delete()
            embed = discord.Embed(
                title="⏳ Thời chờ tái nhận quà đã hết!",
                description=f"{member.mention} hãy phát quà tiếp nào!",
                color=discord.Color.red()
            )
            embed.set_footer(text="Made by Th1nK")
            await channel.send(embed=embed)

async def add_and_remove_role_vip(member):
    temp_role = discord.utils.get(member.guild.roles, id=TEMP_ROLE_ID)
    if temp_role:
        await member.add_roles(temp_role)
        await asyncio.sleep(120)
        await member.remove_roles(temp_role)
        channel = bot.get_channel(VIP_CHANNEL_ID)
        if channel:
            ping_message = await channel.send(f'{member.mention}')
            await asyncio.sleep(1)
            await ping_message.delete()
            embed = discord.Embed(
                title="⏳ Thời chờ tái nhận quà đã hết!",
                description=f"{member.mention} hãy phát quà tiếp nào!",
                color=discord.Color.red()
            )
            embed.set_footer(text="Made by Th1nK")
            await channel.send(embed=embed)


def check_permissions(ctx):
    if ctx.guild.id != ALLOWED_GUILD_ID:
        return False, 'Bot chỉ hoạt động tại server Al1nK SMS.'
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        return False, f'Sms chỉ hoạt động tại kênh <#{ALLOWED_CHANNEL_ID}>.'
    if not has_required_role(ctx.author):
        return False, 'Tuổi gì dùng lệnh?'
    return True, None

@bot.command()
async def sms(ctx, phone_number: str):
    if has_excluded_role(ctx.author):
        await ctx.send("Đang trong thời gian chờ, hãy thử lại sau.")
        return

    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        await ctx.send(f'Sms chỉ hoạt động tại kênh <#{ALLOWED_CHANNEL_ID}>.')
        return

    is_allowed, message = check_permissions(ctx)
    if not is_allowed:
        await ctx.send(message)
        return

    # Nếu là lệnh /smsvip thì bỏ qua
    if ctx.channel.id == VIP_CHANNEL_ID:
        await ctx.send('Lệnh này không thể sử dụng ở kênh VIP. Hãy dùng /smsvip.')
        return

    special_role = discord.utils.get(ctx.guild.roles, id=SPECIAL_ROLE_ID)
    if not phone_number.isnumeric() or (phone_number in INVALID_NUMBERS and special_role not in ctx.author.roles):
        await ctx.send('Số không hợp lệ hoặc không được phép.')
        return

    try:
        file_path = os.path.join(os.getcwd(), "sms.py")
        proc = await asyncio.create_subprocess_exec("python", file_path, phone_number, "120")
        processes.append(proc)

        username = ctx.author.name
        user_id = ctx.author.id
        execution_time = TimeStamp()

        await log_to_channel(username, user_id, phone_number, execution_time)

        embed = discord.Embed(
            title="🎉 Gửi Yêu Cầu Thành Công! 🎉",
            color=0xf78a8a
        )
        embed.add_field(
            name="Thông tin yêu cầu:",
            value=(
                f"📞 **Thuê bao thụ thưởng:** {phone_number}\n"
                f"⚡ **Tốc độ:** Basic\n"
                f"🎁 **Số quà:** 90 hộp\n"
                f"⏳ **Thời nhận tiếp:** 120 giây"
            ),
            inline=False
        )
        embed.set_footer(text=f"Thời gian : {TimeStamp()}")
        embed.set_image(url=get_random_gif_url())

        await ctx.message.reply(embed=embed, mention_author=False)

        await add_and_remove_role(ctx.author)
    except Exception as e:
        await ctx.send(f'Đã xảy ra lỗi khi xử lý lệnh: {e}')

@bot.command()
async def smsvip(ctx, phone_number: str):
    if has_excluded_role(ctx.author):
        await ctx.send("Đang trong thời gian chờ, hãy thử lại sau.")
        return

    # Kiểm tra kênh
    if ctx.channel.id != VIP_CHANNEL_ID:
        await ctx.send(f'Smsvip chỉ hoạt động tại kênh <#{VIP_CHANNEL_ID}>.')
        return

    # Kiểm tra vai trò
    if not discord.utils.get(ctx.author.roles, id=VIP_ROLE_ID):
        await ctx.send('Bạn cần ROLE VIP để sử dụng lệnh này.')
        return

    # Kiểm tra số điện thoại
    special_role = discord.utils.get(ctx.guild.roles, id=SPECIAL_ROLE_ID)
    if not phone_number.isnumeric() or (phone_number in INVALID_NUMBERS and special_role not in ctx.author.roles):
        await ctx.send('Số không hợp lệ hoặc không được phép.')
        return

    try:
        file_path = os.path.join(os.getcwd(), "smsvip.py")
        proc = await asyncio.create_subprocess_exec("python", file_path, phone_number, "120")
        processes.append(proc)

        username = ctx.author.name
        user_id = ctx.author.id
        execution_time = TimeStamp()

        await log_to_channel_vip(username, user_id, phone_number, execution_time)

        embed = discord.Embed(
            title="🎉 Gửi Yêu Cầu Thành Công! 😈",
            color=0xf78a8a
        )
        embed.add_field(
            name="Thông tin yêu cầu:",
            value=(
                f"📞 **Thuê bao thụ thưởng:** {phone_number}\n"
                f"⚡ **Tốc độ:** MAXSPEED\n"
                f"⛓️ **Số lần lặp: 10 lần** \n"
                f"🎁 **Số quà:** 91 hộp\n"
                f"⏳ **Thời nhận tiếp:** 120 giây"
            ),
            inline=False
        )
        embed.set_footer(text=f"Thời gian : {TimeStamp()}")
        embed.set_image(url=get_random_gif_url())

        await ctx.message.reply(embed=embed, mention_author=False)

        await add_and_remove_role_vip(ctx.author)
    except Exception as e:
        await ctx.send(f'Đã xảy ra lỗi khi xử lý lệnh: {e}')

@bot.command()
async def help(ctx):
    is_allowed, message = check_permissions(ctx)
    if not is_allowed:
        await ctx.send(message)
        return

    embed = discord.Embed(
        title="Danh Sách Lệnh",
        color=0xf78a8a
    )
    embed.add_field(name="/sms {số điện thoại}", value="Gửi tin nhắn SMS. (Cần Quyền Hạn)", inline=False)
    embed.add_field(name="/smsvip {số điện thoại}", value="Gửi tin nhắn SMS VIP. (Cần Quyền Hạn)", inline=False)
    embed.set_footer(text="Made by Th1nK")

    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.guild and message.guild.id != ALLOWED_GUILD_ID:
        return

    # Kiểm tra nếu tin nhắn bắt đầu bằng lệnh
    if message.content.startswith('/'):
        # Kiểm tra nếu lệnh không phải là /sms hoặc /help
        if not (message.content.startswith('/sms') or message.content.startswith('/smsvip') or message.content.startswith('/help')):
            if message.channel.id != ALLOWED_CHANNEL_ID:
                await message.channel.send(f'Lệnh chỉ hoạt động tại kênh <#{ALLOWED_CHANNEL_ID}>.')
                return

        # Xử lý lệnh
        await bot.process_commands(message)
    elif isinstance(message.channel, discord.DMChannel):
        await message.channel.send('Bot chỉ hoạt động tại server Al1nK SMS.')

bot.run(TOKEN)

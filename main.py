import discord
from discord.ext import commands
import datetime
import sqlite3
import subprocess
import os
import asyncio
import pytz
import random

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

# Thay thế 'your_token_here' bằng biến môi trường để bảo mật
TOKEN = os.getenv('DISCORD_TOKEN')

# IDs của server và kênh
ALLOWED_CHANNEL_ID = 1264975987934761121
ALLOWED_GUILD_ID = 1264973683877744798
TEMP_ROLE_ID = 1264997863079940170
ROLE_ID = 1264975463672057907

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

# Lưu trữ trạng thái chờ
user_waiting = {}
processes = []  # Danh sách tiến trình

def TimeStamp():
    # Lấy thời gian hiện tại
    now = datetime.datetime.utcnow()  # Lấy giờ UTC hiện tại
    # Chuyển đổi sang giờ Việt Nam (UTC+7)
    vn_time = now + datetime.timedelta(hours=7)
    return vn_time.strftime('%Y-%m-%d %I:%M:%S %p')  # %I sử dụng 12-hour clock và %p để thêm AM/PM

VIDEO_FOLDER = 'video_folder'  # Đường dẫn đến thư mục chứa video của bạn

@bot.event
async def on_ready():
    print(f'Kết nối thành công với {bot.user.name}')

def has_required_role(member):
    role = discord.utils.get(member.guild.roles, id=ROLE_ID)
    return role in member.roles

async def add_and_remove_role(member):
    guild = member.guild
    temp_role = discord.utils.get(guild.roles, id=TEMP_ROLE_ID)
    if temp_role:
        await member.add_roles(temp_role)
        await asyncio.sleep(120)  # Chờ 120 giây
        await member.remove_roles(temp_role)
        channel = bot.get_channel(ALLOWED_CHANNEL_ID)
        if channel:
            ping_message = await channel.send(f'{member.mention}')
            await asyncio.sleep(1)
            await ping_message.delete()
            embed = discord.Embed(
                title="⏳ Thời gian chờ đã kết thúc!",
                description=f"{member.mention} có thể sử dụng tiếp lệnh /sms .",
                color=discord.Color.red()
            )
            embed.set_footer(text="Made by Th1nK")
            await channel.send(embed=embed)

def check_permissions(ctx):
    if ctx.guild.id != ALLOWED_GUILD_ID:
        return False, f'Bot chỉ hoạt động tại server Al1nK SMS.'
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        return False, f'Bot chỉ hoạt động tại kênh <#{ALLOWED_CHANNEL_ID}>.'
    if not has_required_role(ctx.author):
        return False, f'Tuổi gì dùng lệnh?'
    return True, None

@bot.command()
async def sms(ctx, phone_number: str):
    is_allowed, message = check_permissions(ctx)
    if not is_allowed:
        await ctx.send(message)
        return

    if not phone_number.isnumeric() or phone_number in ['113', '911', '114', '115', '84357156328', '0357156328']:
        await ctx.send('Số không hợp lệ hoặc không được phép.')
        return

    try:
        video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.mov', '.avi'))]  # Danh sách các video
        if not video_files:
            await ctx.send('Không tìm thấy video trong thư mục.')
            return

        chosen_video = random.choice(video_files)  # Chọn ngẫu nhiên một video
        file_path = os.path.join(VIDEO_FOLDER, chosen_video)

        embed = discord.Embed(
            title="✨ Yêu cầu tấn công thành công! ✨",
            color=0xf78a8a
        )
        embed.add_field(
            name="Thông tin yêu cầu",
            value=(
                f"📞 **Số điện thoại:** {phone_number}\n"
                f"🔗 **Số API:** 75\n"
                f"⏳ **Thời gian chờ:** **120 giây**"
            ),
            inline=False
        )
        embed.set_footer(text=f"Thời gian : {TimeStamp()}")

        # Gửi embed
        await ctx.send(embed=embed)

        # Gửi video như một tệp đính kèm
        file = discord.File(file_path, filename=chosen_video)
        await ctx.send(file=file)

        await add_and_remove_role(ctx.author)
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
    embed.add_field(name="/sms {số điện thoại}", value="Gửi tin nhắn SMS. (Phải có quyền sử dụng lệnh)", inline=False)
    embed.set_footer(text="Made by Th1nK")

    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.guild and message.guild.id != ALLOWED_GUILD_ID:
        return

    if message.content.startswith('/'):
        if message.channel.id != ALLOWED_CHANNEL_ID:
            await message.channel.send(f'Bot chỉ hoạt động tại kênh <#{ALLOWED_CHANNEL_ID}>.')
            return

        if message.content.startswith('/sms') or message.content.startswith('/help'):
            await bot.process_commands(message)
        else:
            await message.channel.send('Lệnh không xác định, sử dụng lệnh /help để hiện danh sách lệnh.')
    elif isinstance(message.channel, discord.DMChannel):
        await message.channel.send('Bot chỉ hoạt động tại server Al1nK SMS.')
    else:
        return

bot.run(TOKEN)

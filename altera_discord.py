import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

ALLOWED_CHANNEL_ID = 1155409903788240896

ALLOWED_USER_ID = 302050872383242240

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id == ALLOWED_USER_ID:
        await bot.process_commands(message)
        return

    if message.channel.id == ALLOWED_CHANNEL_ID:
        if message.content != "/bump":
            await message.delete()
            await message.channel.send(f"{message.author.mention} ᴏɴʟʏ /ʙᴜᴍᴘ ɪꜱ ᴀʟʟᴏᴡᴇᴅ ɪɴ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ.")
        else:
            await bot.process_commands(message)
    else:
        await bot.process_commands(message)

import os
bot.run(os.environ['TOKEN'])

import os

import discord
from dotenv import load_dotenv

import responses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILDID = os.getenv('DISCORD_GUILD')

def run_discord_bot():
    intents = discord.Intents(messages=True, guilds=True)
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)
    GUILD = client.get_guild(GUILDID)
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        for guild in client.guilds:
            if guild.id == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{message.content}' ({channel})")

        await send_message(message, user_message)

    async def send_message(message, user_message):
        try:
                await message.channel.send(responses.handle_response(user_message))
        except Exception as e:
            print(e)

    client.run(TOKEN)


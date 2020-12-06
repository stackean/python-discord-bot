# bot.py
import os
import discord

MY_DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    # diasble bot self reply
    if message.author == client.user:
        return
        
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
        
@client.event
async def on_ready():
    print('Bot Name:')
    print(client.user.name)
    print(client.user.id)
    print('Bot started...')

client.run(MY_DISCORD_TOKEN)

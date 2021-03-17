#!/usr/bin/env python
# Work with Python 3.6
import discord
from discord.ext import tasks
from ConfigLoader import ConfigLoader

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)


#anything that happens here loops every set minutes
@tasks.loop(minutes=1)
async def loop_msg():
    channel = client.get_channel(STOCK_CHANNEL_ID)
    #await channel.send("I will spam this channel every minute muahaha woof woof")

@client.event
async def on_ready():
    print('Logged in as', end=' ')
    print(client.user.name)
    print('------')
    loop_msg.start()


#load config variables
config_loader = ConfigLoader()
TOKEN = config_loader.getBotToken()
STOCK_CHANNEL_ID =  config_loader.getNewsChannel()

#create client
client.run(TOKEN)



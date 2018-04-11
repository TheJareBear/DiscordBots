import discord

TOKEN = 'NDMyNzM4Njg1ODY0MjQ3Mjk2.Daxq1Q.9WkWZvo9yjc55r2t9WjUdLnlmEI'

client = discord.Client()

@client.event
async def on_message(message):
    check = message.content.lower()
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif check.startswith('!dwight beets'):
        msg = 'BEETS!'.format(message)
        await client.send_message(message.channel, msg)

    elif check.startswith('!dwight hello'):
        msg = 'I do not say hello to my subordinates'.format(message)
        await client.send_message(message.channel, msg)

    elif 'angela' in check:
        msg = 'Angela is a great friend... and also I love her'.format(message)
        await client.send_message(message.channel, msg)

    elif 'jim' in check:
        msg = 'I hate Jim with a burning passion'.format(message)
        await client.send_message(message.channel, msg)

    elif 'dwigt' in check:
        msg = 'My name is Dwight... D-W-I-G-H-T... DWIGHT'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
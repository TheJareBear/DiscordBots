import discord

TOKEN = 'NDMyNzM4Njg1ODY0MjQ3Mjk2.Daxq1Q.9WkWZvo9yjc55r2t9WjUdLnlmEI'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('dwight'):
        msg = '/tts BEETS!'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
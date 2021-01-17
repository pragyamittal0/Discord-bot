

import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('hello'):
    await message.channel.send('Hey!')
  if msg.startswith('how are you'):
    await message.channel.send('I am good. You tell')
  if msg.startswith('I am fine. Thank you'):
    await message.channel.send('My pleasure!')


client.run('ODAwMTM5MTU3ODA0MDIzODcw.YANxqQ.D-xFCqK1GMq7z4Xx9ZQyqtN2BRs')
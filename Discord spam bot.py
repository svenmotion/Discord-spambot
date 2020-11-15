import discord
client = discord.Client()
keywords = ["Hi", "hi", "Test", "test", "Discord", "discord"]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
          for j in range(6):
              await message.channel.send("Get spammed by a bot")


client.run('Discord bot token')

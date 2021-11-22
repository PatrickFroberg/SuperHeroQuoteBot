import discord
from configparser import ConfigParser
from SuperHeroQuotesService import SuperHeroQuotesService


client = discord.Client()
config = ConfigParser()

config.read('config.ini')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
          .format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
            return

        if message.content.lower().startswith('!quote'):
            await message.channel.send(SuperHeroQuotesService.get_random_quote())


client.run(config['DiscordBotSettings']['Token'])
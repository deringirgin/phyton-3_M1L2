import discord
from discord.ext import commands
from config import TOKEN
from ejdarha import Ejderha

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)


@client.command()
async def info(ctx):
    ejder = Ejderha("Alev", "Kırmızı")
    await ctx.send(ejder.bilgi())


@client.command()
async def saldır(ctx):
    ejder = Ejderha("Toothless", "Siyah")
    await ctx.send(ejder.ates_puskur())


@client.command()
async def savun(ctx):
    ejder = Ejderha("Light Fury", "Beyaz")
    await ctx.send(ejder.savun())


@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')
client.run(TOKEN)

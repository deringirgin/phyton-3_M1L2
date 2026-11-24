import discord
from discord.ext import commands
from config import TOKEN
from ejdarha import Ejderha

intents = discord.Intents.default()
intents.message_content = True

# Özel help komutunun çakışmaması için help_command=None eklendi
client = commands.Bot(command_prefix='/', intents=intents, help_command=None)


@client.event
async def on_ready():
    print(f'Giriş yaptı: {client.user}')


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


@client.command()
async def repeat(ctx, sayi: int, *, mesaj: str):
    if sayi < 1 or sayi > 10:
        await ctx.send("Lütfen 1 ile 10 arasında bir sayı girin.")
        return

    for _ in range(sayi):
        await ctx.send(mesaj)


@client.command()
async def help(ctx):
    yardim_mesaji = (
        "**Yardım Menüsü**\n"
        "1. `/info` : Ejderha ile ilgili bilgi verir.\n"
        "2. `/saldır` : Ejderha saldırır.\n"
        "3. `/savun` : Ejderha savunma yapar.\n"
        "4. `/about` : Bot bilgisi verir.\n"
        "5. `/repeat [sayı] [mesaj]` : Mesajı belirtilen sayıda tekrarlar."
    )
    await ctx.send(yardim_mesaji)


client.run(TOKEN)

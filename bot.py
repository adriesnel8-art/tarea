import discord
from discord.ext import commands

# permisos del bot
intents = discord.Intents.default()
intents.message_content = True

# creacion del bot
botsito = commands.Bot(command_prefix='!', intents=intents)

@botsito.event
async def on_ready():
    print(f'Bot conectado como {botsito.user}')

@botsito.command()
async def hola(ctx):
    await ctx.send('Hola! ¿En qué puedo ayudarte?')
    





# Inicia el bot con tu token
botsito.run('TU_TOKEN_AQUI')

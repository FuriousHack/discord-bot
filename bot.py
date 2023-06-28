import discord
from discord.ext import commands

# Créer une instance du bot avec les intents
intents = discord.Intents.default()
intents.typing = False  # Désactiver la réception des événements "typing" (facultatif, vous pouvez le laisser activé si vous le souhaitez)
intents.presences = False  # Désactiver la réception des événements de présence (facultatif, vous pouvez le laisser activé si vous le souhaitez)

bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

# Commande ping
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Latence en millisecondes
    await ctx.send(f'Pong! Latence : {latency:.2f}ms')

# Démarrer le bot
bot.run('MTEyMzI2MDI2NDU1NzU4NDU2NQ.GaOp-y.NpNg6ZeEVTtMhFSgQvpnCtB0zZeQ5GMeXRmvUM')

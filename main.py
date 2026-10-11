
from token import token
import discord
from discord.ext import commands
import requests
import pyttsx3

# =========================
# INICIALIZAÇÃO
# =========================

engine = pyttsx3.init()

bot = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all()
)


# =========================
# SÍNTESE DE FALA
# =========================

def speak(text):
    engine.say(text)
    engine.runAndWait()


# =========================
# COMANDO DE BOAS-VINDAS
# =========================

@bot.command()
async def start(ctx):
    mensagem = f"Olá, {ctx.author.name}! Seja bem-vindo ao bot de curiosidades!"
    await ctx.send(mensagem)


# =========================
# BUSCAR CURIOSIDADE NA API
# =========================

def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            dados = response.json()
            print(dados)

            return dados.get("text", "Não foi possível encontrar uma curiosidade.")

        return None

    except requests.RequestException:
        return None


# =========================
# COMANDO DE CURIOSIDADE
# =========================

@bot.command()
async def fact(ctx):
    curiosidade = get_fact()

    if curiosidade is None:
        await ctx.send(
            "Não foi possível buscar uma curiosidade. Tente novamente mais tarde."
        )
        return

    mensagem = f"🔎 Curiosidade: {curiosidade}"

    await ctx.send(mensagem)

    # Lê a curiosidade em voz alta
    speak(curiosidade)


# =========================
# INICIAR O BOT
# =========================

bot.run(token)

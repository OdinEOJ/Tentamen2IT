import discord
from discord.ext import commands, tasks
import requests
import datetime
from discord.utils import get
import random
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
tall = random.randint(1,5)

CHANNEL_ID = 1335885165355864148
TARGET_USER_ID = 648178003628654612

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    hey.start()


@tasks.loop(seconds=60)
async def hey():
    now = datetime.datetime.now()
    if now.hour == 8 and now.minute == 20:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(f"@everyone God morn cock suckers mother fuckers")

@bot.command()
async def money(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Get yo money up not yo funny up👹💸👹💸👹")

@bot.command()
async def randimg(ctx):
    folder_path = "bot\\bilder"
    
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    
    selected_image = random.choice(image_files)
    
    file_path = os.path.join(folder_path, selected_image)
    file = discord.File(file_path)
    await ctx.send(file=file)

@bot.event
async def on_message(message):
    if message.author.id == TARGET_USER_ID and not message.author.bot:
        await message.channel.send("Omagawd, mobbing iris...")


@bot.command()
async def weather(ctx):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/complete?altitude=10&lat=66.1985&lon=13.0350"
    headers = {"Accept": "application/json", "User-Agent": "MyWeatherApp/1.0 (odinelias07@gmail.com)"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        temperatur = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
        vind = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]
        vindkast = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed_of_gust"]
        nedbør = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["details"]["precipitation_amount"]
        torden = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["details"]["probability_of_thunder"]

        vindEmoji = "🌪️" if vind >= 10 else "🍃"
        temperaturEmoji = "☀️" if temperatur >= 10 else "🥶" if temperatur <= 10 else "⛄"

        message = (
            "**Her er værforholdene på Nesna akkurat nå:**\n"
            f"Temperatur: {temperatur} °C  {temperaturEmoji}\n"
            f"Vind: {vind} m/s, og {vindkast} m/s i vindkastene  {vindEmoji}\n"
            f"Nedbør: {nedbør} mm 🌧️\n"
            f"Det er også en {torden}% sjanse for torden! ⚡"
        )

        await ctx.send(message)
    else:
        await ctx.send(f"❌ Feil {response.status_code}: Kunne ikke hente været akkurat nå. Prøv igjen senere! 😭")
    

TOKEN = ""
bot.run(TOKEN)

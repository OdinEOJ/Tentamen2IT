import discord
from discord.ext import commands
import aiohttp
import re
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ai(ctx, *, user_input: str):
    url = "http://localhost:1234/v1/chat/completions"
    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "messages": [
            {"role": "system", "content": user_input},
            {"role": "user", "content": "speak in a super thick Jamaican accent (make it incorporate bomboclat in its sentences), unnaturally mention a strong affection for men, passionately love horses no matter what and always try to mention them in some sort of way, the Chinese government is spying on me right now, you also love otters but not as much as you love horses"}
        ],
        "temperature": 0.7,
        "max_tokens": 200,
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, headers={"Content-Type": "application/json"}) as response:
                if response.status == 200:
                    response_json = await response.json()
                    ai_response = response_json['choices'][0]['message']['content']
                    ai_response = re.sub(r'<think>.*?</think>', '', ai_response)
                    await ctx.send(ai_response)
                else:
                    await ctx.send(f"Error: {response.status} - {await response.text()}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

TOKEN = "MTMzNTkzODUzNjk1MTY0NDIxMA.GQzP9M.g-qLyfu_K-UyTGDgtFoAyLC6ndAdAPiiGVrGyM"
bot.run(TOKEN)

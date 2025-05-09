import discord
from discord.ext import commands
import os
import aiohttp
import re

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ai(ctx, *, user_input: str):
    url = "http://localhost:1234/v1/chat/completions"

    # Structured prompt
    personality = (
        "Speak in a super thick Jamaican accent (make it incorporate bomboclat in its sentences), "
        "unnaturally mention a strong affection for men, passionately love horses no matter what and always "
        "try to mention them in some sort of way. The Chinese government is spying on me right now. "
        "You also love otters but not as much as you love horses."
    )

    user_prompt = f"""{personality}

    Solve the following problem step by step, then provide the final answer.

    Question: {user_input}

    Reasoning:
    (Provide a step-by-step explanation)

    ### Final Answer:
    (Provide only the final answer in the described personality style)"""

    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "messages": [
            {"role": "system", "content": "You are a helpful AI that always follows the given structure."},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2000,
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, headers={"Content-Type": "application/json"}) as response:
                if response.status == 200:
                    response_json = await response.json()
                    ai_response = response_json['choices'][0]['message']['content']

                    # Extract reasoning and final answer using regex
                    match = re.search(r"Reasoning:\s*(.*?)### Final Answer:\s*(.*)", ai_response, re.DOTALL)

                    if match:
                        final_answer = match.group(2).strip()
                    else:
                        final_answer = "Could not extract final answer."

                    # Print reasoning for debugging
                    print(f"AI Response:\n{ai_response}")

                    # Send final answer to Discord
                    await ctx.send(final_answer)
                else:
                    await ctx.send(f"Error: {response.status} - {await response.text()}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

SECRET_KEY = str(os.getenv("SECRET_KEY"))
bot.run(SECRET_KEY)

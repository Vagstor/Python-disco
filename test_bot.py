# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()  # Create an instance of Intents
client = discord.Client(intents=intents)  # pass the intents


@client.event
async def on_ready():  # Checking for connection
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_member_join(member):  # Auto-responding to member joining (DM)
    await member.create_dm()
    await member.dm_channel.send(f"привет {member.name}, как дела?")


@client.event
async def on_message(message):  # Auto-responding to member writing anything
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        "Да ну тебя нахуй",
        "Ты че болен?",
        "Братан, ты поехавший блять",
        "Вызывайте дурку!",
        "Что это такое и зачем мне это нужно?",
        "Если бы ты знал как мне похуй, ты бы расплакался.",
        "Твое отличие от фашиста разве что на рентгене можно разглядеть...",
    ]

    if message.content:
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "С Днем рождения" in message.content:
        response = f"Поздравляю, {message.mentions[0]}! 🎈🎉"
        await message.channel.send(response)
    elif message.content == "raise-exception":
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):  # Handling exceptions related to messages
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise


client.run(TOKEN)

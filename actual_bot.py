# bot.py
import random

import discord
from discord.ext.commands import Bot, context
import discord.ext.commands
from discord.member import Member
from discord.message import Message

from config import settings
from constants import constant
import discord.ext

intents = discord.Intents.all()

bot = Bot(command_prefix="!", intents=intents)
client = discord.Client(intents=intents)


@bot.event
async def on_ready():  # Checking for connection
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="random_quote", help="Случайные цитаты из Disco Elysium")
async def random_quote(ctx: context.Context):
    response = random.choice(constant.RANDOM_DISCO_QUOTES)
    await ctx.send(response)

@bot.command(name="random_meme", help="Случайный мем по Disco Elysium")
async def random_meme(ctx: context.Context):
    response = random.choice(constant.RANDOM_DISCO_MEMES)
    await ctx.send(response)


@bot.command(name="roll_dice", help="Бросок кубика (стандартное значение: один D6)")
async def roll(ctx: context.Context, number_of_dice: int = discord.ext.commands.parameter(default = 1, description = "Количество бросков"), number_of_sides: int = discord.ext.commands.parameter(default = 6, description= "Количество сторон")):
    number_of_dice_ceiled = min(number_of_dice, 5)  # limit number of dices?
    dices = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice_ceiled)
    ]
    for dice in dices:
        images = constant.DICE_IMAGE_MAPPING.get(int(dice))
        if images is not None:
            await ctx.send(random.choice(images))
    await ctx.send(", ".join(dices))


@bot.event
async def on_member_join(member: Member):  # Auto-responding to member joining (DM)
    await member.create_dm()
    await member.dm_channel.send(f"Привет {member.name}, как дела?")


# @bot.event
# async def on_message(message: Message):  # Автоматический ответ на сообщение, в котором фигурирует ну или давай
#     if message.author == bot.user:
#         return

#     if message.content == "ну":
#         response = random.choice(constant.BROOKLYN_99_QUOTES)
#         await message.channel.send(response)
#     return


# @client.event
# async def on_message(message: Message):
#     if message.author == client.user:
#         return
#     if "С Днем рождения" in message.content:
#         response = f"Поздравляю, {message.mentions[0]}! 🎈🎉"
#         await message.channel.send(response)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):  # Handling exceptions related to messages
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise


bot.run(settings.TOKEN)
# client.run(settings.TOKEN)

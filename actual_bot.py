# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents_bot = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents_bot)

intents = discord.Intents.all() # Create an instance of Intents
client = discord.Client(intents=intents) # pass the intents

@bot.event
async def on_ready(): # Checking for connection
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="disco", help='Цитаты из Disco Elysium')
async def random_quote(ctx):
    random_quotes = [
        'Если бы вы знали как Куно похуй, вы бы расплакались.',
        'Твое отличие от фашиста разве что на рентгене можно разглядеть...',
        'Это и есть настоящая тьма. Не смерть, не война, не насилие над детьми. У настоящей тьмы лицо любви. Первая смерть случается в сердце, Гарри.',
        'ОТЛИЧНО ПОДОЙДЕТ ПТИЦАМ ВЫСОКОГО ПОЛЕТА. ЛЮБИТЕЛЯМ ТУСОВОК. КОПАМ, КОТОРЫМ НУЖНА ИСКРА.',
        'Отправляйтесь на планету тусовок. Вы любите наркотики, и это взаимно.',
        'А не пойти ли тебе нахер прямо сейчас, а?',
        'Вот теперь она напугана. Поняла, что правда имеет дело с умственно неполноценным.',
        'Внутренняя империя[Просто: Успех] Отбой! Ты это явно не подумавши. То, что ты там увидишь, тебе не понравится — а развидеть это ты уже не сможешь.',
        'Я не *просто* расист. Слушай, я читал *книги*.',
        'Конечно, я не терял свою тушку... То есть пушку! Бляха... Не терял я свой пистолет!',
        'Я же тебе говорил, боров. Куно не торчит в захолустье. Куно бывал в таких местах, о которых ты и мечтать не мог.'
    ]
    response = random.choice(random_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Бросок кубика')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    dice_images = {
        20: ['https://i.postimg.cc/QCpvqpJ1/1.gif',
             'https://images.stopgame.ru/uploads/images/210114/form/2017/01/09/1483964682.gif',
             ],
        6: ['https://hellfiredesigns.wordpress.com/wp-content/uploads/2012/09/rollin_d61.gif',
            'https://www.richardhughesjones.com/wp-content/uploads/2019/01/dice-gif.gif'
        ]
    }
    try:
        await ctx.send(random.choice(dice_images[number_of_sides]))
        await ctx.send(', '.join(dice))
    except:
        await ctx.send(', '.join(dice))

# @client.event
# async def on_member_join(member): # Auto-responding to member joining (DM)
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'привет {member.name}, как дела?'
#     )

# @client.event
# async def on_message(message): # Auto-responding to member writing anything
#     if message.author == client.user:
#         return

#     brooklyn_99_quotes = [
#         'Да ну тебя нахуй',
#         'Ты че болен?',
#         'Братан, ты поехавший блять',
#         'Вызывайте дурку!',
#         'Что это такое и зачем мне это нужно?',
#         'Если бы ты знал как мне похуй, ты бы расплакался.',
#         'Твое отличие от фашиста разве что на рентгене можно разглядеть...'
#     ]

#     if message.content:
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)

# @client.event
# async def on_message (message):
#     if message.author == client.user:
#         return
#     if "С Днем рождения" in message.content:
#         response = f"Поздравляю, {message.mentions[0]}! 🎈🎉"
#         await message.channel.send(response)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
    
# @client.event
# async def on_error(event, *args, **kwargs): # Handling exceptions related to messages
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

bot.run(TOKEN)
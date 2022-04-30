import discord
from discord.ext import commands


# /* --- Init & boot confirm --- */ #
bot = commands.Bot(command_prefix = '>>') #Set command prefix

@bot.event
async def on_ready():
    print('Major Tom to Ground control') #Boot confirmation

#Context test, returns arg
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


# /* --- Anti-bottom brigade --- */ #
@bot.event
async def on_message(message):
    if message.author == bot.user: #Stop bot from replying to itself
        return

    if message.content.has(':pleading:'):
        await message.channel.send('Haha bottom')

#bot.run('') #//TODO: A token lmao
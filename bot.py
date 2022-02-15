from colorama import Fore, init
import discord
from discord.ext import *
from discord.ext import commands
client = commands.Bot( command_prefix = '+')

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount)
    await ctx.channel.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений!', color = 0x11806a))

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ping(ctx):
    await ctx.send('Блинб, мой пинг: {0}'.format(client.latency)) 

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def sclear(ctx, amount: int):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.purge(limit = amount)

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member,*,reason = 'Banned by operator'):
    await user.ban(reason=reason)
    await ctx.channel.send(f'{user} забанен по причине' + reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed = discord.Embed(title = 'Ошибка!', description = f':no_entry_sign: {ctx.author.name}, ты полнйший лох!', color = 0x11806a))

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed = discord.Embed(title = 'Ошибка!', description = f':no_entry_sign: {ctx.author.name}, обязательно введите аргумент!', color = 0x11806a))
        
#запуск
client.run( '' )
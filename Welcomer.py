import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

TOKEN = ""

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

def random_color():
    return discord.Color(random.randint(0, 0xFFFFFF))

 # Welcomer
 
@client.event
async def on_member_join(member):
    channel_id = 1336703321523621940 #replace to your channel ID
    channel = client.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title="Welcome!", 
            description=f"Hello {member.mention}, Welcome To The Our Server", 
            color=random_color() 
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_author(name=member.name, icon_url=member.avatar.url)
        embed.add_field(name="Members:", value=f"{member.guild.member_count}", inline=False)
        embed.set_footer(text="Powered By (name)")
        await channel.send(embed=embed)

client.run(TOKEN)


'''
Instructions for python.... Copy all into a file named: ‘membercount.py’

1) Create discord application:
    https://discordapp.com/developers/applications/

2) Authorize application on your server:
    https://discordapp.com/oauth2/authorize?client_id=<app-id>&scope=bot&permissions=8

3) Install discord from CLI:
    $ python3.7 -m pip install discord.py

4) Run app from CLI....
    $ python3.7 membercount.py
'''
import discord
import sites #required: sites/__init__.py

TOKEN = sites.cDiscordTOKEN
client = discord.Client()

memberCnt = 0
cmdCnt = 0

@client.event
async def on_member_join(member):
    global memberCnt
    memberCnt += 1

@client.event
async def on_member_remove(member):
    global memberCnt
    memberCnt -= 1

@client.event
async def on_message(message):
    global cmdCnt

    # do not consider bot msgs
    if message.author == client.user:
        return

    strMsg = message.content
    if strMsg[0:] == ‘!’:
    cmdCnt += 1

client.run(TOKEN)

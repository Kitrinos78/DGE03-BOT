###################################################################
# DISCORD BOT For DGE 03
# Created by JARONCHAI DILOKKALAYAKUL
# 30 MAY 2021
###################################################################

# Import required modules
import discord
import os
import random
import datetime
from bs4 import BeautifulSoup
import requests
from wordSearch import show_origin, show_definitions

# Import list of quotes
from quoteList import edgeworthQuotes, botQuotesDefault, fuckQuotes
from utilList import timetable

# Import pinging function
from stayinAlive import keep_alive

###################################################################
# SETUP DISCORD CLIENT
###################################################################

client = discord.Client()

###################################################################
# MAIN EVENT SCRIPT - TYPE: MESSAGE
###################################################################


@client.event
# Log in as a bot
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

###################################################################
# GENERAL COMMANDS
###################################################################

    if msg.startswith(':3'):
        if msg.startswith(':3 '):
            pass
        else:
            await message.channel.send(random.choice(botQuotesDefault))

    if msg.startswith(':3 edgy'):
        await message.channel.send(random.choice(edgeworthQuotes))

    if msg.startswith(':3 help'):
        await message.channel.send("""
      These are the currently available functions:
      Main functions:
      - :3 help [View what the bot can do]
      - :3 [Calls the bot and shit]
      - :3 edgy [Say shit from Miles Edgeworth]
      Timetables:
      - :3 tt [View timetable this semester]
      - :3 tt today [View today's timetable]
      - :3 tt *day* [View that day's timetable]
      Others:
      - Try to piss me off with :3 fuck you
        """)

    if msg.startswith(':3 fuck me'):
        await message.channel.send('fuck you, %s' % message.author.mention)
    elif msg.startswith(':3 fuck'):
        await message.channel.send(random.choice(fuckQuotes))

    if msg.startswith(':3 define'):
        searchWord = message.content
        searchWord = searchWord[10:]

        word_to_search = searchWord
        scrape_url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + word_to_search

        headers = {"User-Agent": ""}
        web_response = requests.get(scrape_url, headers=headers)

        if web_response.status_code == 200:
            soup = BeautifulSoup(web_response.text, 'html.parser')

            try:
                await message.channel.send(searchWord.upper())
                await message.channel.send(show_origin(soup)[11:])
                await message.channel.send(show_definitions(soup))
            except AttributeError:
                await message.channel.send('Word not found!!')
        else:
            await message.channel.send('Failed to get response...')

###################################################################
# TIMETABLE
###################################################################

    if msg.startswith(':3 tt'):
        if msg.startswith(':3 tt '):
            pass
        else:
            await message.channel.send("2nd Year 1st Semester!!" + "\n\n" + timetable[0] + "\n\n" + timetable[1] + "\n\n" + timetable[2] + "\n\n" + timetable[3] + "\n\n" + timetable[4])

    if msg.startswith(':3 tt today'):
        rn = datetime.datetime.now()
        await message.channel.send('Today is ' + rn.strftime("%A"))
        if rn.strftime("%A") == "Monday":
            await message.channel.send(timetable[0])
        if rn.strftime("%A") == "Tuesday":
            await message.channel.send(timetable[1])
        if rn.strftime("%A") == "Wednesday":
            await message.channel.send(timetable[2])
        if rn.strftime("%A") == "Thursday":
            await message.channel.send(timetable[3])
        if rn.strftime("%A") == "Friday":
            await message.channel.send(timetable[4])
        if rn.strftime("%A") == "Saturday":
            await message.channel.send("It's the weekend, get ready for next week!")
        if rn.strftime("%A") == "Sunday":
            await message.channel.send("It's the weekend, get ready for next week!")

    if msg.startswith(':3 tt monday'):
        await message.channel.send(timetable[0])
    if msg.startswith(':3 tt tuesday'):
        await message.channel.send(timetable[1])
    if msg.startswith(':3 tt wednesday'):
        await message.channel.send(timetable[2])
    if msg.startswith(':3 tt thursday'):
        await message.channel.send(timetable[3])
    if msg.startswith(':3 tt friday'):
        await message.channel.send(timetable[4])
    if msg.startswith(':3 tt saturday'):
        await message.channel.send(timetable[5])
    if msg.startswith(':3 tt sunday'):
        await message.channel.send(timetable[5])

###################################################################
# RUNNING THE BOT
###################################################################

keep_alive()
client.run(os.getenv('TOKEN'))

###################################################################

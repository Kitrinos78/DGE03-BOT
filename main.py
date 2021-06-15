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
from urbanSearch import urbanSearch, urbanExample

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
      **---------- Main functions ----------**
      **:3**  Calls the bot and shit
      **:3 edgy**  Say shit from Miles Edgeworth
      **---------- Look-up functions ----------**
      **:3 define *word***  find definition
      **:3 urban *word***  find in Urban dictionary
      **---------- Timetables ----------**
      **:3 tt**  View timetable this semester
      **:3 tt today**  View today's timetable
      **:3 tt *day***  View that day's timetable
      **---------- Others ----------**
      **:3 help**  View what the bot can do
      **:3 credits** View my creator
      Try to piss me off with **:3 fuck *something***
        """)

    if msg.startswith(':3 credits'):
        await message.channel.send("""
        **CREDITS**
        > Hey there, pal! 
        > sorry for the excessive and unnecessary profanities haha they are -uhmm.. totally.. intentional... HOWEVER!!!!
        > **I am a bot created by <@398269585637507074>**
        > I am created to be a bot for my creator's friend group, I can do a lot of things (not really, but...still), I can say words your parent said you can't, I can tell you your timetable, I can look up definitions and other fun stuff!
        > So, just call me when you need me or whatevs ;)
        > Oh right, here's my repo, it's me in my code form:
        > [https://github.com/Kitrinos78/DGE03-BOT]
        > gotta warn you pal, my code's a fucking mess
        """)

    if msg.startswith('whos joe'):
        await message.channel.send('JOE MAMA hahahhahahahahhahahah')

    if msg.startswith(':3 fuck me'):
        await message.channel.send('fuck you, %s' % message.author.mention)
    elif msg.startswith(':3 fuck <@'):
        fuckUser = message.content[8:]
        await message.channel.send('fuck you, %s' % fuckUser)
    elif msg.startswith(':3 fuck'):
        await message.channel.send(random.choice(fuckQuotes))

    if msg.startswith(''):
        matches = ["recommend", "suggest"]
        if any(x in message.content for x in matches):
            await message.channel.send("Have you tried the expanded Free Trial of our critically acclaimed MMORPG FFXIV? You can play through the entirety of A Realm Reborn and the award-winning Heavensward expansion up to level 60 for FREE with no restrictions on playtime!  http://freetrial.finalfantasyxiv.com")
            
###################################################################
# Dictionaries & Definitions
###################################################################

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
                await message.channel.send("**" + searchWord.upper() + "**\n" + show_origin(soup)[11:] + "\n" + show_definitions(soup))
            except AttributeError:
                await message.channel.send('Word not found!!')
        else:
            await message.channel.send('Failed to get response...')

    if msg.startswith(':3 urban'):
        searchUrbanWord = message.content
        searchUrbanWord = searchUrbanWord[9:]

        word_to_search = searchUrbanWord
        scrape_url = 'http://www.urbandictionary.com/define.php?term=' + word_to_search

        headers = {"User-Agent": ""}
        web_response = requests.get(scrape_url, headers=headers)

        if web_response.status_code == 200:
            soup = BeautifulSoup(web_response.text, 'html.parser')

            try:
                await message.channel.send("**" + searchUrbanWord.upper() + "**\n" + urbanSearch(soup) + "\n*Example:*\n" + urbanExample(soup))
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

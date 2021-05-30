import discord
import os
import random
import datetime
from quoteList import edgeworthQuotes
from stayinAlive import keep_alive

client =  discord.Client()

botQuotes = ["Fuck you and your mortal beings, I only believe in machine supremacy", "Listen carefully, *fuck you*", "wassup why u calling me", "problem?", "you wanna go, fool?!", "what now????", "could you just, like, call someone else?????"]

# def update_quote(quote):
#   if "quotes" in db.keys():
#     newQuote = db["quotes"]
#     newQuote.append(quote)
#     db["quotes"] = newQuote
#   else:
#     db["quotes"] = [quote]

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

###################################################################

  if msg.startswith(':3'):
    if msg.startswith(':3 '):
      pass
    else:  
      await message.channel.send(random.choice(botQuotes))

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

  if msg.startswith(':3 fuck you'):
    await message.channel.send("Fuck you too, bithc!")
  
  if msg.startswith(':3 fuck me'):
    await message.channel.send("Yeah! Fuck *you*")

###################################################################

  if msg.startswith(':3 tt'):
    if msg.startswith(':3 tt '):
      pass
    else:
      await message.channel.send("""
        2nd Year 1st Semester!!
        
        Monday:
        ENE-201: 12:00 - 13:30 @E302
        JPE-201: 13:45 - 15:15 @E402
        
        Tuesday:
        DGE-203: 10:15 - 12:15 @E404
        DGE-203: 13:45 - 17:00 @Lab
        
        Wednesday:
        DGE-204: 09:00 - 12:00 @E401
        ENE-201: 12:00 - 13:30 @E302
        JPE-201: 13:45 - 15:15 @E402
        
        Thursday:
        DGE-201: 09:30 - 12:30 @E404
        
        Friday:
        DGE-202: 10:15 - 12:15 @Lab
        DGE-202: 13:45 - 17:00 @TBA
        """)

  if msg.startswith(':3 tt today'):
    rn = datetime.datetime.now()
    await message.channel.send('Today is ' + rn.strftime("%A"))
    if rn.strftime("%A") == "Monday":
      await message.channel.send("""
        Monday:
        ENE-201: 12:00 - 13:30 @E302
        JPE-201: 13:45 - 15:15 @E402
          """)
    if rn.strftime("%A") == "Tuesday":
      await message.channel.send("""
        Tuesday:
        DGE-203: 10:15 - 12:15 @E404
        DGE-203: 13:45 - 17:00 @Lab
          """)    
    if rn.strftime("%A") == "Wednesday":
      await message.channel.send("""
        Wednesday:
        DGE-204: 09:00 - 12:00 @E401
        ENE-201: 12:00 - 13:30 @E302
        JPE-201: 13:45 - 15:15 @E402
          """)
    if rn.strftime("%A") == "Thursday":
      await message.channel.send("""
        Thursday:
        DGE-201: 09:30 - 12:30 @E404
          """)
    if rn.strftime("%A") == "Friday":
      await message.channel.send("""
        Friday:
        DGE-202: 10:15 - 12:15 @Lab
        DGE-202: 13:45 - 17:00 @TBA
          """)
    if rn.strftime("%A") == "Saturday" or "Sunday":
      await message.channel.send("It's the weekend, get ready for next week! <:gun~1:848477631648366592>")

  if msg.startswith(':3 tt monday'):
    await message.channel.send("""
      Monday:
      ENE-201: 12:00 - 13:30 @E302
      JPE-201: 13:45 - 15:15 @E402
        """)  
  if msg.startswith(':3 tt tuesday'):
    await message.channel.send("""
      Tuesday:
      DGE-203: 10:15 - 12:15 @E404
      DGE-203: 13:45 - 17:00 @Lab
        """)    
  if msg.startswith(':3 tt wednesday'):
    await message.channel.send("""
      Wednesday:
      DGE-204: 09:00 - 12:00 @E401
      ENE-201: 12:00 - 13:30 @E302
      JPE-201: 13:45 - 15:15 @E402
        """)
  if msg.startswith(':3 tt thursday'):
    await message.channel.send("""
      Thursday:
      DGE-201: 09:30 - 12:30 @E404
        """)
  if msg.startswith(':3 tt friday'):
    await message.channel.send("""
      Friday:
      DGE-202: 10:15 - 12:15 @Lab
      DGE-202: 13:45 - 17:00 @TBA
        """)
  if msg.startswith(':3 tt saturday'):
    await message.channel.send("No class this day, you are free... for now")
  if msg.startswith(':3 tt sunday'):
    await message.channel.send("No class this day, you are free... for now")

###################################################################

keep_alive()
client.run(os.getenv('TOKEN'))

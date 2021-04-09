import discord
import os
import requests
import json
import random

client = discord.Client()

#WORDS TO LOOK FOR AND REPLY TO
sad_words = ["sad", "unhappy", "depressing"]

#ENCOURAGING WORDS
starter_encouragments = [
  "chear up.",
  "Hang in there.",
  "your a greate person."
]
#COURCE WORDS 
curse = ['i can hack', 'i will hack you']

#GETTING QUOTE FROM THE API AND FORMATING IT
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

#REPLYING TO $QUOTE COMMAND
  if msg.startswith("$quote"):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragments))

#CURCE WORDS
  if any(word in msg for word in curse):
    await message.channel.send("""Shut up i'll hack your moms IP and ddos your balls, then i'm gonna put you on r/masterhacker you piece of shit skid. Get a life.""")

client.run('ODI3MjQ0NTkyNTc1MTUyMTgw.YGYNkA.NReWCZk3PogxF9YrCgaa_hdzEJY')
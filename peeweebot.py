import discord
import os
import time
import random


def generateSecretWord():
    wordListFile = open("wordlist", "r")
    words = wordListFile.readlines()
    random.seed()
    global secretWord
    global secretWordTime
    secretWord= words[random.randint(0,999)].strip("\n")
    secretWordTime = time.strftime("%j")
    print("Don't tell anyone, the secret word is " + secretWord)
    return()





generateSecretWord()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if (secretWordTime != time.strftime("%j")):
        generateSecretWord()
    if (secretWord.lower() in message.content.lower()) and (message.author.bot is False):
        gif = open("/home/travis/Downloads/pee-wee-silly.gif",'rb')
        await message.channel.send(content =message.author.name.upper() + " SAID " + secretWord.upper() + "! " + message.author.name.upper() + " SAID THE SECRET WORD!", file = discord.File(gif))

client.run('[token]')

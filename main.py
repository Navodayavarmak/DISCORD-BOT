import os
import discord
import datetime
import asyncio
import pyjokes
from keep_alive import keep_alive

messages = joined = 0
my_secret = os.environ['token']
joke = pyjokes.get_joke("en", "all")
client = discord.Client()


def ran_joke():
    joke = pyjokes.get_joke("en", "all")
    return joke

def finder(test_word,known_words) :
    out = any(word in test_word for word in known_words)
    return out

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(
                    f"TIME : {datetime.datetime.now()}, MESSAGES : {messages} ,MEMBERS : {joined}\n"
                )

            messages = 0
            joined = 0

            await asyncio.sleep(600)

        except Exception as e:
            print(e)
            await asyncio.sleep(600)


@client.event
async def on_ready():
    with open("stats.txt", "a") as f:
        f.write(
            f"We have logged in as {client.user} on {datetime.datetime.now()} \n"
        )
        print("BOT IS ONLINE...")


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("navodaya") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="nONE one")


@client.event
async def on_member_join(member):

    global joined
    joined += 1

    for channel in member.guild.channels:
        if str(channel) == "general":
            await client.send_message(f"Welcome to the server {member.mention}"
                                      )


@client.event
async def on_message(message):

    global messages
    messages += 1

    id = client.get_guild(935853226782232576)
    channels = ["general", "prison"]
    channels1 = ["general"]
    channels2 = ["prison"]
    commands = ["!users", "!joke", "!help", "!details"]
    valid_users = ["Navodaya#5068", "NV BOT#2793"]
    punch = ["alive","online","Online","Alive","ONLINE","ALIVE"]
    sendoffs = ["Bye","bye","Night","GN","gn","Gn","Good night","Taruvatha","bye bye"]
    commons = ["Ha","ha","Hmm","hmm","mm","kk","OK","Ok","k","K","Kk","KK","kk","ok"]
    word9 = ["bot","Bot","BOT","Thank you","thanks","thanks bot"]
    pins = ["Varma","Navodaya","navodaya","NVK","nvk","NV","nv","varma","VARMA","NAVODAYA"]
    greetings = [
        "hi", "HI", "Hi", "HII", "Hii", "hii", "GM", "Good","good", "Good morning",
        "Hello"
    ]
    bad_words = ["18+", "bad", "fuck", "bsdk", "wtf", "what the..."]
    admin_commands = ["!delete all", "!delete 20"]

    #words = open("badwords.txt","r")
    #bad_words=words.read()
    #words.close()

    for word in bad_words:
        if message.content.count(word) > 0:
            with open("history.txt", "a") as f:
                f.write(
                    f"The message was deleted(bad word) {message.content} from {message.author} \n"
                )
                await message.channel.purge(limit=1)

    if str(message.channel) in channels2 and str(message.content) in commands:

        if str(message.content) == "!users":
            await message.channel.send(f"TOTAL NO OF USERS : {id.member_count}"
                                       )

        elif str(message.content) == "!joke":
            await message.channel.send(ran_joke())

        elif str(message.content) == "!details" :
          await message.channel.send("HELLO ! IM BOT, SPEED :ACCORDING TO UR MSG,MEMORY :UNLIMITED BCZ CLOUD ! ")

        elif message.content == "!help":
            embed = discord.Embed(title="HEY HOW CAN I HELP YOU?",
                                  description="I CAN HELP BY THESE COMMANDS")
            embed.add_field(name="!users", value="GIVES TOTAL OF USERS")
            embed.add_field(name="!joke", value="GIVES A JOKE")
            embed.add_field(name="!help", value="GIVES LIST OF COMMANDS")
            embed.add_field(name="HI,hii,NAMASTY", value="GREET THE USERS")
            embed.add_field(name="!details", value="BASIC INFO ABOUT ME")
            embed.add_field(name="admin_commands", value="!delete all,!delete 20")
            await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels:
      if str(message.content) in greetings:
        
            await message.channel.send("HI GOOD TO SEE YOU AGAIN! ")

    if str(message.channel) in channels and str(message.author) not in valid_users:
      if str(message.content) in punch:
            await message.channel.send(" NENU AMARUDUNI RA ! ")

    if str(message.channel) in channels and str(message.author) not in valid_users:
      if str(message.content) in sendoffs :
            await message.channel.send(" AM VUNDHI LE IKA PADUKO ! ") 

    if str(message.channel) in channels and str(message.author) not in valid_users:
      if str(message.content) in commons :
            await message.channel.send(" NUV MARAVA APUDU AVE IKA ! ")

    if str(message.channel) in channels and str(message.author) in valid_users:
      if str(message.content) in word9  :
            await message.channel.send(" THATS MY PLEASURE,BOSS ! ")

    if str(message.channel) in channels :
      if str(message.content) in pins :
            await message.channel.send("BOSS RECEIVED YOUR MESSAGE,HE WILL REPLY AS SOON AS POSSIBLE!")        

    if str(message.channel) in channels1:
        if str(message.content) in commands:
            print(
                f"USER : {message.author} tried to do command {message.content} "
            )
            await message.channel.send(
                "HII THERE! GOOD TO SEE YOU TRY PERFORMING THE ACTION IN PRISON CHANNEL"
            )

    if str(message.channel) in channels and str(message.author) in valid_users:

        if str(message.content) in admin_commands and str(
                message.content) == "!delete all":
            with open("history.txt", "a") as f:
                f.write(
                    f"All message was deleted by {message.author} on {datetime.datetime.now()} \n"
                )
                await message.channel.purge(limit=100)

        elif str(message.content) in admin_commands and str(
                message.content) == "!delete 20":
            with open("history.txt", "a") as f:
                f.write(
                    f"20 message was deleted by {message.author} on {datetime.datetime.now()} \n"
                )
                await message.channel.purge(limit=20)

keep_alive()
client.loop.create_task(update_stats())
client.run(my_secret)

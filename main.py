import discord
import os
from keep_alive import keep_alive
import wikipedia
import wikia 

###########################################################################

client = discord.Client()

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event


async def on_message(message):
      
  if message.author == client.user:
    return

  if "hey ein" in message.content.lower():
    await message.channel.send("Bork Bork")
  
  if "!wiki" in message.content.lower():
    words = message.content.split()
    searchCrit = words[1:]
    await message.channel.send(wiki_summary(searchCrit))
  
  if message.content.startswith("!anime"):
    searchCrit = message.content[7:]
    await message.channel.send(anime_search(searchCrit))
  
  if message.content.startswith("!poketype"):
    searchCrit = message.content[10:]
    await message.channel.send(Poke_Type(searchCrit))

  if message.content.startswith("!einhelp"):
    await message.channel.send(ein_help())

########################################################################

def wiki_summary(arg):
  definition = wikipedia.summary(arg, sentences=1, chars=100, 
  auto_suggest=True, redirect=True)
  return definition

def anime_search(arg):
  info = wikia.summary("anime", arg)
  if info.startswith("redirect"):
    info = wikia.summary("anime", info[8:])
  return info

def Poke_Type(arg):

  typeStats = {"normal":("Strong Against: NOTHING", 
                          "Weak Against: Rock, Ghost, Steel",
                          "Resistant to: Ghost",
                          "Vulnerable to: Fighting"),
                "fighting":("Strong Against: Normal, Rock, Steel, Ice, Dark", 
                          "Weak Against: Flying, Poison, Psychic, Bug, Ghost, Fairy",
                          "Resistant to: Rock, Bug, Dark",
                          "Vulnerable to: Flying, Psychic, Fairy"),
                "flying":("Strong Against: Fighting, Bug, Grass	", 
                          "Weak Against: Rock, Steel, Electric",
                          "Resistant to: Fighting, Ground, Bug, Grass",
                          "Vulnerable to: Rock, Electric, Ice"),
                "poison":("Strong Against: Grass, Fairy	", 
                          "Weak Against: Poison, Ground, Rock, Ghost, Steel",
                          "Resistant to: Fighting, Poison, Grass, Fairy",
                          "Vulnerable to: Ground, Psychic"),
                "ground":("Strong Against: Poison, Rock, Steel, Fire, Electric", 
                          "Weak Against: Flying, Bug, Grass	",
                          "Resistant to: Poison, Rock, Electric",
                          "Vulnerable to: Water, Grass, Ice"),
                "rock":("Strong Against: Flying, Bug, Fire, Ice", 
                          "Weak Against: Fighting, Ground, Steel",
                          "Resistant to: Normal, Flying, Poison, Fire",
                          "Vulnerable to: Fighting, Ground, Steel, Water, Grass"),
                "bug":("Strong Against: Grass, Psychic, Dark", 
                          "Weak Against: Fighting, Flying, Poison, Ghost, Steel, Fire, Fairy",
                          "Resistant to: Fighting, Ground, Grass",
                          "Vulnerable to: Flying, Rock, Fire"),
                "ghost":("Strong Against: Ghost, Psychic", 
                          "Weak Against: Normal, Dark",
                          "Resistant to: Normal, Fighting, Poison, Bug",
                          "Vulnerable to: Ghost, Dark"),                     
                "steel":("Strong Against: Rock, Ice, Fairy", 
                          "Weak Against: Steel, Fire, Water, Electric",
                          "Resistant to: Normal, Flying, Poison, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, Fairy",
                          "Vulnerable to: Fighting, Ground, Fire"),
                "fire":("Strong Against: Bug, Steel, Grass, Ice", 
                          "Weak Against: Rock, Fire, Water, Dragon",
                          "Resistant to: Bug, Steel, Fire, Grass, Ice	",
                          "Vulnerable to: Ground, Rock, Water"),
                "water":("Strong Against: Ground, Rock, Fire", 
                          "Weak Against: Water, Grass, Dragon",
                          "Resistant to: Steel, Fire, Water, Ice",
                          "Vulnerable to: Grass, Electric"),
                "grass":("Strong Against: Ground, Rock, Water", 
                          "Weak Against: Flying, Poison, Bug, Steel, Fire, Grass, Dragon",
                          "Resistant to: Ground, Water, Grass, Electric",
                          "Vulnerable to: Flying, Poison, Bug, Fire, Ice"),   
                "electric":("Strong Against: Flying, Water", 
                          "Weak Against: Ground, Grass, Electric, Dragon",
                          "Resistant to: Flying, Steel, Electric",
                          "Vulnerable to: Ground"),  
                "psychic":("Strong Against: Fighting, Poison", 
                          "Weak Against: Steel, Psychic, Dark	",
                          "Resistant to: Fighting, Psychic",
                          "Vulnerable to: Bug, Ghost, Dark"),
                "ice":("Strong Against: Flying, Ground, Grass, Dragon", 
                          "Weak Against: Steel, Fire, Water, Ice",
                          "Resistant to: Ice",
                          "Vulnerable to: Fighting, Rock, Steel, Fire"),
                "dragon":("Strong Against: Dragon", 
                          "Weak Against: Steel, Fairy",
                          "Resistant to: Fire, Water, Grass, Electric",
                          "Vulnerable to: Ice, Dragon, Fairy"),
                "fairy":("Strong Against: Fighting, Dragon, Dark", 
                          "Weak Against: Poison, Steel, Fire",
                          "Resistant to: Fighting, Bug, Dragon, Dark",
                          "Vulnerable to: Poison, Steel"),
                "dark":("Strong Against: Ghost, Psychic", 
                          "Weak Against: Fighting, Dark, Fairy",
                          "Resistant to: Ghost, Psychic, Dark",
                          "Vulnerable to: Fighting, Bug, Fairy"),  
                "???":("stop", "it", "now", "Chris"),                                             
                "head": "ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ \n\n",
                "foot": "\n\nϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩"                           
  }

  if arg.lower() in typeStats:
  
    stats = typeStats["head"] + str(typeStats[arg.lower()][0]) + "\n"  + str(typeStats[arg.lower()][1]) + "\n"  + str(typeStats[arg.lower()][2]) + "\n"  + str(typeStats[arg.lower()][3]) + typeStats["foot"]

    return stats
  
  else:

    stats = "Type not in database"

    return stats

def ein_help():
  
  info = "¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥ \n\n hey ein: returns 'Bork Bork' \n !wiki: searches wikipedia and returns a summary \n !anime: searches anime fandom and returns summary \n !poketype: searches database and returns a pokemon type's strengths and weaknesses \n !einhelp: returns this masterpiece \n\n ¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥¥[*.*]¥ "

  return info

##########################################################################

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

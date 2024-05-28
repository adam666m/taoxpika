import os
import re
import time
import multiprocessing
import datetime
import random
# copyright to poketwolover69
import keep_alive
# copyright to poketwolover69
# copyright to poketwolover69
import discum
from discum.utils.button import Buttoner

version = '0.0'

owner_id = 1005663711123493025
channel_id = 1237231239849840691
catch_id = 1237231239849840691
with open('pokemon.txt', 'r', encoding='utf8') as file:
    pokemon_list = file.read()
with open('legendary.txt', 'r') as file:
    legendary_list = file.read()
with open('mythical.txt', 'r') as file:
    mythical_list = file.read()
with open('level.txt', 'r') as file:
    to_level = file.readline()

num_pokemon = 0
shiny = 0
legendary = 0
mythical = 0

poketwo_id = '716390085896962058'
bot = discum.Client(
    token='', log=False)
keep_alive.keep_alive()


def solve(message):
    hint = []
    for i in range(15, len(message) - 1):
        if message[i] != '\\':
            hint.append(message[i])
    hint_string = ''
    for i in hint:
        hint_string += i
    solution = re.findall('^'+hint_string.replace('_', '.') +
                          '$', pokemon_list, re.MULTILINE)
    return solution


def spam():
    while True:
        contenttt = random.getrandbits(128)
        bot.sendMessage('1237231260485550101', contenttt)
        intervals = [3.0, 3.0, 3.0, 3.0] #best interval for spawns in poketwo bot
        time.sleep(random.choice(intervals))


def start_spam():
    new_process = multiprocessing.Process(target=spam)
    new_process.start()
    return new_process


def stop(process):
    process.terminate()


def log(string):
    now = datetime.datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print(f'[{current_time}]', string)


@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:
        log(f'the account is now active!\nlogged into: {bot.gateway.session.user["username"]}')


@bot.gateway.command
def on_message(resp):
    global spam_process
    if resp.event.message:
        m = resp.parsed.auto()
        if m['channel_id'] == '1237231239849840691':
            if m['author']['id'] == '716390085896962058':
                if m['embeds']:
                    embed_title = m['embeds'][0]['title']
                    if 'wild pokémon has appeared!' in embed_title:
                        stop(spam_process)
                        time.sleep(1)
                        bot.sendMessage('1237231239849840691', message='<@716390085896962058> h')
                    elif "Congratulations" in embed_title:
                        embed_content = m['embeds'][0]['description']
                        if 'now level' in embed_content:
                            stop(spam_process)
                            split = embed_content.split(' ')
                            a = embed_content.count(' ')
                            level = int(split[a].replace('!', ''))
                            if level == 100:
                                bot.sendMessage(
                                    channel_id, f"<@716390085896962058> s {to_level}")
                                with open('level.txt', 'r') as fi:
                                    data = fi.read().splitlines(True)
                                with open('level.txt', 'w') as fo:
                                    fo.writelines(data[1:])
                                spam_process = start_spam()
                            else:
                                spam_process = start_spam()
                else:
                    content = m['content']
                    if 'The pokémon is ' in content:
                        if len(solve(content)) == 0:
                            log('Pokemon not found.')
                        else:
                            for i in solve(content):
                                stop(spam_process)
                                time.sleep(1)
                                bot.sendMessage(
                                    '1237231239849840691', message=f'<@716390085896962058> c {i}')
                        time.sleep(1)
                        spam_process = start_spam()

                    elif 'Congratulations' in content:
                        global shiny
                        global legendary
                        global num_pokemon
                        global mythical
                        num_pokemon += 1
                        split = content.split(' ')
                        pokemon = split[7].replace('!', '')
                        if 'These colors seem unusual...' in content:
                            shiny += 1
                            log(
                                f'A shiny Pokémon was caught! Pokémon: {pokemon}')
                            log(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        elif re.findall('^'+pokemon+'$', legendary_list, re.MULTILINE):
                            legendary += 1
                            log(
                                f'A legendary Pokémon was caught! Pokémon: {pokemon}')
                            log(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        elif re.findall('^'+pokemon+'$', mythical_list, re.MULTILINE):
                            mythical += 1
                            log(
                                f'A mythical Pokémon was caught! Pokémon: {pokemon}')
                            log(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        else:
                            print(f'Total Pokémon Caught: {num_pokemon}')

                    elif 'human' in content:
                        bot.sendMessage('1237231239849840691', message=f'<@1005663711123493025> please solve the captcha')
                        stop(spam_process)
                        log('Captcha Detected; Autocatcher Paused. Press enter to restart.')
                        input()
                       


@bot.gateway.command
def on_message(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        if m['channel_id'] == '1243902555809906720':
            if m['author']['id'] == '1243897906344497284':
             content = m['content']
             if '$bal' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> bal')
             elif '$quest' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> q')
             elif '$profile' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> profile')
             elif '$pokemon' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> p')
             elif '$sh' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> p --sh')
             elif '$myth' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> p --my')
             elif '$leg' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> p --leg')
             elif '$spd' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> p --spdiv 31')
             elif '$trade' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> t <@1005663711123493025>')
             elif '$tc' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> t c')
             elif '$taa' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> t aa --3000')
             elif '$help' in content:
               bot.sendMessage('1243902555809906720', message='```HELP MENU:\n__$bal__ : displays poketwo balance\n__$quest__ : displays poketwo quests\n__$profile__ : displays p2 profile\n__$pokemon__ : shows all the pokemons\n__$sh__ : displays shinies caught\n__$leg__ : shows legendary mons caught\n__$myth__ : shows mythical mons caught\n__$spd__ : displayed speed 31 mons\n__$trade__ : sends trade prompt\n__$tc__ : confirms trade')
             elif '$pika' in content:
               bot.sendMessage('1243902555809906720', message='<@716390085896962058> p --n pikachu --n pichu --n raichu')
             elif '$pc' in content:
               split = content.split(' ')
               pc = split[1]
               bot.sendMessage('1243902555809906720', message=f'<@716390085896962058> t a pc {pc}')
             elif '$mb' in content:
               split = content.split(' ')
               mb = split[1]
               bot.sendMessage('1243902555809906720', message=f'<@716390085896962058> m b {mb}')
             elif '$pk' in content:
               split = content.split(' ')
               pK = split[1]
               bot.sendMessage('1243902555809906720', message=f'<@716390085896962058> t a {pK}')
             elif '$go' in content:
               split = content.split(' ')
               g0 = split[1]
               bot.sendMessage('1243902555809906720', message=f'<@716390085896962058> go {g0}')
             elif '$info' in content:
               split = content.split(' ')
               info = split[1]
               bot.sendMessage('1243902555809906720', message=f'<@716390085896962058> i {info}')
             elif '$select' in content:
               split = content.split(' ')
               slc = split[1]
               bot.sendMessage('1243902555809906720', message=f'<@716390085896962058> s {slc}')
            else:
                  log('lmso gay')
@bot.gateway.command
def buttonclicker(resp):
        if resp.event.message or resp.event.message_updated:
            m = resp.parsed.auto()
            try:
                if m['author']['id'] == '716390085896962058':
                    if len(m["components"]) > 0:
                        content = m['content']
                        if 'Are you sure you want to buy this' in content:
                                buts = Buttoner(m['components'])
                         
                                bot.click(
                                      m["author"]["id"],
                                      channelID=m["channel_id"],
                                      guildID=m.get('guild_id'),
                                      messageID=m["id"],
                                      messageFlags=m["flags"],
                                      data=buts.getButton(row=0, column=0)
                                  )
            except:
                pass 
@bot.gateway.command
def buttonclicker(resp):
        if resp.event.message or resp.event.message_updated:
            m = resp.parsed.auto()
            try:
                if m['author']['id'] == '716390085896962058':
                    if len(m["components"]) > 0:
                        content = m['content']
                        if 'Are you sure you want to trade' in content:
                                buts = Buttoner(m['components'])
                         
                                bot.click(
                                      m["author"]["id"],
                                      channelID=m["channel_id"],
                                      guildID=m.get('guild_id'),
                                      messageID=m["id"],
                                      messageFlags=m["flags"],
                                      data=buts.getButton(row=0, column=0)
                                  )
            except:
                pass 



if __name__ == '__main__':
    print(
        f'poketwo autocatcher has been started.\nautocatcher version: {version}\nevent log:')
    spam_process = start_spam()
    bot.gateway.run(auto_reconnect=True)

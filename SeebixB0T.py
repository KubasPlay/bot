import discord
import asyncio
import random
import time

TOKEN = 'NTEzNDgyNjE2MzI2OTc5NTg1.DtIqMw.CdQ8o_aSUN9OeAf99RUz6KRpEpk'

client = discord.Client()

prefix = 'S!'
ping = '<@356346393612517379>'
wersja = 'v1.1 BETA'

@client.event
async def on_ready():
    print('Wszystko dziala jak powinno :)')
    await client.change_presence(game=discord.Game(name='Prefix to s! | '+(wersja)+' by KubasPlay'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.upper().startswith((prefix)+'BOT'):
        embed=discord.Embed(title=" ", color=0x00ff00)
        embed.set_author(name="O bocie", icon_url="https://yt3.ggpht.com/a-/AN66SAxeyoCXnygPUU53fZmCg2BGMLM0sECLI_mFSA=s900-mo-c-c0xffffffff-rj-k-no")
        embed.add_field(name='Autor:', value='KubasPlay#5714', inline=True)
        embed.add_field(name='Wersja:', value=wersja, inline=True)
        embed.add_field(name='Prefix:', value=prefix, inline=True)
        embed.add_field(name='Pomoc:', value='KubasPlay#5714', inline=True)
        await client.send_message(message.channel, embed=embed)

    elif message.content.upper().startswith((prefix)+'KOMENDY'):
        embed=discord.Embed(title=" ", color=0xffff00)
        embed.set_author(name="Komendy: Ogólne", icon_url="https://i.imgur.com/9xaDFiZ.png")
        embed.add_field(name='s!bot - informacje o bocie', value='s!komendy - wysyła tą listę na DM', inline=False)
#        embed.add_field(name='!dg komenda - opis', value='!dg [pytanie] - zadaje pytanie botowi', inline=False)
#        embed.add_field(name='!dg komenda - opis', value='!dg info - wysyła na pv listę komend', inline=False)
        await client.send_message(message.author, embed=embed)
        embed=discord.Embed(title=" ", color=0xff0000)
        embed.set_author(name="Komendy: Zabawa", icon_url="https://i.imgur.com/hb38N1B.png")
        embed.add_field(name='s!<pytanie> - zadaj pytanie botowi', value='s!komenda - opis', inline=False)
#        embed.add_field(name='!dg komenda - opis', value='!dg komenda - opis', inline=False)
#        embed.add_field(name='!dg komenda - opis', value='!dg komenda - opis', inline=False)
        await client.send_message(message.author, embed=embed)
        msg = ':ballot_box_with_check: | {0.author.mention} wysłałem ci komendy na pv :)'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.upper().startswith((prefix)+'CZY'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Nie.", "Tak.", "Nie pytaj mnie o to.", "Nie odpowiem. Czytam prasę komputerową."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'LUBISZ'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Nie.", "Tak.", "Nie pytaj mnie o to.", "Nie odpowiem. Piję kawę."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'JAK'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Normalnie...", "W dziwny sposób.", "Nie pytaj mnie o to.", "Nie odpowiem. Piję kawę."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'GDZIE'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Na ławce.", "W parku.", "Na krześle.", "W kubku od kawy."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'KIEDY'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Miesiąc temu.", "Dawno, dawno temu.", "Wczoraj.", "Nie odpowiem."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'SKĄD'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Stąd.", "Z książki.", "Nie pytaj mnie o to.", "Nie odpowiem. Piję kawę."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'DOKĄD'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Tam.", "Nie pytaj mnie o to.", "Nie odpowiem. Rozwiązuję krzyżówkę."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'DLACZEGO'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Bo tak.", "A czemu by nie?", "Proszę Cię! Nie pytaj mnie o to.", "Nie odpowiem. Piję kawę."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'KTO'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Twój kuzyn.", "Twoja mama.", "Twój tata.", "Pewnie KubasPlay."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'CZEMU'):
        tmp = await client.send_message(message.channel, ':thinking:')
        time.sleep(2)
        messages = ["Bo tak."]
        await client.edit_message(tmp, random.choice(messages))

    elif message.content.upper().startswith((prefix)+'WIADOMOSCI'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Liczenie wiadomości...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'Napisałeś/aś {} wiadomości.'.format(counter))

    elif 'kurw' in message.content:
        msg = ':warning: Ej, ty tam! {0.author.mention} nie przeklinaj!'.format(message)
        await client.send_message(message.channel, msg)

    elif 'dziwk' in message.content:
        msg = ':warning: Ej, ty tam! {0.author.mention} nie przeklinaj!'.format(message)
        await client.send_message(message.channel, msg)

    elif 'jeba' in message.content:
        msg = ':warning: Ej, ty tam! {0.author.mention} nie przeklinaj!'.format(message)
        await client.send_message(message.channel, msg)

    elif 'pierda' in message.content:
        msg = ':warning: Ej, ty tam! {0.author.mention} nie przeklinaj!'.format(message)
        await client.send_message(message.channel, msg)

    elif 'pierdo' in message.content:
        msg = ':warning: Ej, ty tam! {0.author.mention} nie przeklinaj!'.format(message)
        await client.send_message(message.channel, msg)
        
    elif 'huj' in message.content:
        msg = ':warning: Ej, ty tam! {0.author.mention} nie przeklinaj!'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.upper().startswith((prefix)+'KANALY'):
        msg = 'Zgubiłeś się wśród kanałów głosowych na tym serwerze? My ci w tym pomożemy!\n**KANAŁY BEZLIMITU**\n#1 bezlimitu **s!bezlimitu1**\n**KANAŁY GŁOSOWE**\nKANAŁ MUZYCZNY **s!muzyczny**\nAFK **s!afk**\nCentrum Pomocy **s!centrumpomocy**\n**KANAŁY MAX. 2-5**\n#1 Max [2 os.] **s!1max2**\n#2 Max [2 os.] **s!2max2**\n#3 Max [2 os.] **s!3max2**'
        await client.send_message(message.channel, msg)

    elif message.content.upper().startswith((prefix)+'BEZLIMITU1'):
        channel = discord.utils.find(lambda x: x.name == '#1 bezlimitu', message.server.channels)
        await client.move_member(message.author, channel)

    elif message.content.upper().startswith((prefix)+'MUZYCZNY'):
        channel = discord.utils.find(lambda x: x.name == 'KANAŁ MUZYCZNY', message.server.channels)
        await client.move_member(message.author, channel)

    elif message.content.upper().startswith((prefix)+'AFK'):
        channel = discord.utils.find(lambda x: x.name == 'AFK', message.server.channels)
        await client.move_member(message.author, channel)

    elif message.content.upper().startswith((prefix)+'CENTRUMPOMOCY'):
        channel = discord.utils.find(lambda x: x.name == 'Centrum Pomocy', message.server.channels)
        await client.move_member(message.author, channel)

    elif message.content.upper().startswith((prefix)+'1MAX2'):
        channel = discord.utils.find(lambda x: x.name == '#1 Max [2 os.]', message.server.channels)
        await client.join_member(message.author, channel)

    elif message.content.upper().startswith((prefix)+'2MAX2'):
        channel = discord.utils.find(lambda x: x.name == '#2 Max [2 os.]', message.server.channels)
        await client.move_member(message.author, channel)

    elif message.content.upper().startswith((prefix)+'3MAX2'):
        channel = discord.utils.find(lambda x: x.name == '#3 Max [2 os.]', message.server.channels)
        await client.move_member(message.author, channel)

client.run(TOKEN)

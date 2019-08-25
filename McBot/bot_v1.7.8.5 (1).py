import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix = "`")
bot.remove_command("help")
m = "dirt"
l = 1
x = 0
tl = 0
stime = 0
minecoins = 0
pick = 1
woodp = 1
stonep = 0
goldp = 0
ironp = 0
diamondp = 0
rxp = 50
sel = 0
dirt = 0
stone = 0
coal = 0
gold = 0
iron = 0
lapiz = 0
redstone = 0
diamond = 0
emerald = 0
bedrock = 0
dirta = 0
stonea = 0
coala = 0
golda = 0
irona = 0
lapiza = 0
redstonea = 0
diamonda = 0
emeralda = 0
bedrocka = 0
tsel = 0

async def mdirt():
    global x
    global dirt
    global dirta
    dirta = dirta+1
    dirt = dirt+1
    x = x+5*pick

async def mstone():
    global x
    global stone
    global stonea
    stonea = stonea+1
    stone = stone+1
    x = x+10*pick

async def mcoal():
    global x
    global coal
    global coala
    coala = coala+1
    coal = coal+1
    x = x+15*pick

async def mgold():
    global x
    global gold
    global golda
    golda = golda+1
    gold = gold+1
    x = x+20*pick

async def miron():
    global x
    global iron
    global irona
    irona = irona+1
    iron = iron+1
    x = x+25*pick

async def mlapiz():
    global x
    global lapiz
    global lapiza
    lapiza = lapiza+1
    lapiz = lapiz+1
    x = x+30*pick

async def mredstone():
    global x
    global redstone
    global redstonea
    redstonea = redstonea+1
    redstone = redstone+1
    x = x+35*pick

async def mdiamond():
    global x
    global diamond
    global diamonda
    diamonda = diamonda+1
    diamond = diamond+1
    x = x+40*pick

async def memerald():
    global x
    global emerald
    global emeralda
    emeralda = emeralda+1
    emerald = emerald+1
    x = x+50*pick

async def mbedrock():
    global x
    global bedrock
    global bedrocka
    bedrocka = bedrocka+1
    bedrock = bedrock+1
    x = x+100*pick

async def rdirt():
    number = random.randint(1,100)
    if number == 1:
        await mstone()
    else:
        await mdirt()

async def rstone():
    number = random.randint(1,100)
    if number < 76:
        await mdirt()
    elif number > 75 and number < 99:
        await mstone()
    else:
        await mcoal()

async def rcoal():
    number = random.randint(1,100)
    if number < 26:
        await mdirt()
    elif number > 25 and number < 76:
        await mstone()
    elif number > 75 and number < 99:
        await mcoal()
    else:
        await mgold()

async def rgold():
    number = random.randint(1,100)
    if number < 21:
        await mdirt()
    elif number > 20 and number < 61:
        await mstone()
    elif number > 60 and number < 91:
        await mcoal()
    else:
        await mgold()

async def riron():
    number = random.randint(1,100)
    if number < 11:
        await mdirt()
    elif number > 10 and number < 31:
        await mstone()
    elif number > 30 and number < 51:
        await mcoal()
    elif number > 50 and number < 71:
        await mgold()
    elif number > 70 and number < 91:
        await miron()
    else:
        await mlapiz()

async def rlapiz():
    number = random.randint(1,100)
    if number < 6:
        await mdirt()
    elif number < 16:
        await mstone()
    elif number < 26:
        await mcoal()
    elif number < 36:
        await mgold()
    elif number < 46:
        await miron()
    elif number < 56:
        await mlapiz()
    elif number < 76:
        await mredstone()
    elif number < 91:
        await mdiamond()
    elif number < 100:
        await memerald()
    else:
        await mbedrock()

async def rredstone():
    number = random.randint(1,100)
    if number < 6:
        await mdirt()
    elif number < 11:
        await mstone()
    elif number < 21:
        await mcoal()
    elif number < 31:
        await mgold()
    elif number < 41:
        await miron()
    elif number < 51:
        await mlapiz()
    elif number < 71:
        await mredstone()
    elif number < 91:
        await mdiamond()
    elif number < 96:
        await memerald()
    else:
        await mbedrock()

async def rdiamond():
    number = random.randint(1,100)
    if number < 2:
        await mstone()
    elif number < 7:
        await mcoal()
    elif number < 12:
        await mgold()
    elif number < 21:
        await miron()
    elif number < 31:
        await mlapiz()
    elif number < 41:
        await mredstone()
    elif number < 61:
        await mdiamond()
    elif number < 81:
        await memerald()
    else:
        await mbedrock()

async def remerald():
    number = random.randint(1,100)
    if number < 6:
        await miron()
    elif number < 11:
        await mlapiz()
    elif number < 21:
        await mredstone()
    elif number < 41:
        await mdiamond()
    elif number < 71:
        await memerald()
    else:
        await mbedrock()

async def rbedrock():
    number = random.randint(1,100)
    if number < 6:
        await mlapiz()
    elif number < 11:
        await mredstone()
    elif number < 21:
        await mdiamond()
    elif number < 41:
        await memerald()
    else:
        await mbedrock()

async def lup(ctx):
    global l
    global x
    global rxp
    if x >= rxp:
        x = 0
        rxp = rxp+50
        l = l+1
        embed=discord.Embed(title="Level up!", description="", colour=discord.Color.green(), url="")
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("Bot is logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Game(name="`help"))

@bot.command()
async def mine(ctx):
    global stime
    if stime == 0:
        global dirta, stonea, coala, golda, irona, lapiza, redstonea, diamonda, emeralda, bedrocka
        dirta = 0
        stonea = 0
        coala = 0
        golda = 0
        irona = 0
        lapiza = 0
        redstonea = 0
        diamonda = 0
        emeralda = 0
        bedrocka = 0
        if m == "dirt":
            if pick == 1:
                await rdirt()
            elif pick == 2:
                await rdirt()
                await rdirt()
            elif pick == 3:
                await rdirt()
                await rdirt()
                await rdirt()
            elif pick == 4:
                await rdirt()
                await rdirt()
                await rdirt()
                await rdirt()
            else:
                await rdirt()
                await rdirt()
                await rdirt()
                await rdirt()
                await rdirt()
        elif m == "stone":
            if pick == 1:
                await rstone()
            elif pick == 2:
                await rstone()
                await rstone()
            elif pick == 3:
                await rstone()
                await rstone()
                await rstone()
            elif pick == 4:
                await rstone()
                await rstone()
                await rstone()
                await rstone()
            else:
                await rstone()
                await rstone()
                await rstone()
                await rstone()
                await rstone()
        elif m == "coal":
            if pick == 1:
                await rcoal()
            elif pick == 2:
                await rcoal()
                await rcoal()
            elif pick == 3:
                await rcoal()
                await rcoal()
                await rcoal()
            elif pick == 4:
                await rcoal()
                await rcoal()
                await rcoal()
                await rcoal()
            else:
                await rcoal()
                await rcoal()
                await rcoal()
                await rcoal()
                await rcoal()
        elif m == "gold":
            if pick == 1:
                await rgold()
            elif pick == 2:
                await rgold()
                await rgold()
            elif pick == 3:
                await rgold()
                await rgold()
                await rgold()
            elif pick == 4:
                await rgold()
                await rgold()
                await rgold()
                await rgold()
            else:
                await rgold()
                await rgold()
                await rgold()
                await rgold()
                await rgold()
        elif m == "iron":
            if pick == 1:
                await riron()
            elif pick == 2:
                await riron()
                await riron()
            elif pick == 3:
                await riron()
                await riron()
                await riron()
            elif pick == 4:
                await riron()
                await riron()
                await riron()
                await riron()
            else:
                await riron()
                await riron()
                await riron()
                await riron()
                await riron()
        elif m == "lapiz":
            if pick == 1:
                await rlapiz()
            elif pick == 2:
                await rlapiz()
                await rlapiz()
            elif pick == 3:
                await rlapiz()
                await rlapiz()
                await rlapiz()
            elif pick == 4:
                await rlapiz()
                await rlapiz()
                await rlapiz()
                await rlapiz()
            else:
                await rlapiz()
                await rlapiz()
                await rlapiz()
                await rlapiz()
                await rlapiz()
        elif m == "redstone":
            if pick == 1:
                await rredstone()
            elif pick == 2:
                await rredstone()
                await rredstone()
            elif pick == 3:
                await rredstone()
                await rredstone()
                await rredstone()
            elif pick == 4:
                await rredstone()
                await rredstone()
                await rredstone()
                await rredstone()
            else:
                await rredstone()
                await rredstone()
                await rredstone()
                await rredstone()
                await rredstone()
        elif m == "diamond":
            if pick == 1:
                await rdiamond()
            elif pick == 2:
                await rdiamond()
                await rdiamond()
            elif pick == 3:
                await rdiamond()
                await rdiamond()
                await rdiamond()
            elif pick == 4:
                await rdiamond()
                await rdiamond()
                await rdiamond()
                await rdiamond()
            else:
                await rdiamond()
                await rdiamond()
                await rdiamond()
                await rdiamond()
                await rdiamond()
        elif m == "emerald":
            if pick == 1:
                await remerald()
            elif pick == 2:
                await remerald()
                await remerald()
            elif pick == 3:
                await remerald()
                await remerald()
                await remerald()
            elif pick == 4:
                await remerald()
                await remerald()
                await remerald()
                await remerald()
            else:
                await remerald()
                await remerald()
                await remerald()
                await remerald()
                await remerald()
        else:
            if pick == 1:
                await rbedrock()
            elif pick == 2:
                await rbedrock()
                await rbedrock()
            elif pick == 3:
                await rbedrock()
                await rbedrock()
                await rbedrock()
            elif pick == 4:
                await rbedrock()
                await rbedrock()
                await rbedrock()
                await rbedrock()
            else:
                await rbedrock()
                await rbedrock()
                await rbedrock()
                await rbedrock()
                await rbedrock()
        embed = discord.Embed(title="You Mined:", description="", colour=discord.Color.green(), url="")
        if dirta > 0:
            embed.add_field(name="----------", value=f"<:dirt:614479214967783450> Dirt: x{dirta}", inline=False)
        if stonea > 0:
            embed.add_field(name="----------", value=f"<:stone:614479264393461780> Stone: x{stonea}", inline=False)
        if coala > 0:
            embed.add_field(name="----------", value=f"<:coal:614479289525600275> Coal: x{coala}", inline=False)
        if golda > 0:
            embed.add_field(name="----------", value=f"<:gold:614479398510264330> Gold: x{golda}", inline=False)
        if irona > 0:
            embed.add_field(name="----------", value=f"<:iron:614479445377679380> Iron: x{irona}", inline=False)
        if lapiza > 0:
            embed.add_field(name="----------", value=f"<:lapis:614479424645234690> Lapis: x{lapiza}", inline=False)
        if redstonea > 0:
            embed.add_field(name="----------", value=f"<:redstone:614480910502330368> Redstone: x{redstonea}", inline=False)
        if diamonda > 0:
            embed.add_field(name="----------", value=f"<:diamond:614480931612393476> Diamond: x{diamonda}", inline=False)
        if emeralda > 0:
            embed.add_field(name="----------", value=f"<:emerald:614480949752758305> Emerald: x{emeralda}", inline=False)
        if bedrocka > 0:
            embed.add_field(name="----------", value=f"<:bedrock:614480966844678151> Bedrock: x{bedrocka}", inline=False)
        await ctx.send(embed=embed)
        await lup(ctx)
        stime = 3
        await asyncio.sleep(1)
        stime = 2
        await asyncio.sleep(1)
        stime = 1
        await asyncio.sleep(1)
        stime = 0
    elif stime == 1:
        embed=discord.Embed(title="You must wait 1 more second before using that command again.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"You must wait {stime} more seconds before using that command again.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands:", description="help:                 Displays a list of commands.\n\nlvl:                  Checks your lvl.\n\nmine:                 Mines in the mine that you are in.\n\nswitch:               Allows you to switch mines.\n\nmines:                Shows a list of mines.\n\ncheck {mine}:         Checks the block chances in that mine.\n\ninventory:            Shows you how many blocks you have.\n\nequip {item}:         Equips that item.\n\nsell {item}:          Sells all of that item.\n\nshop:                 Checks the shop.\n\nbuy {item} {amount}:  buys that amount of the item.\n\nbalance:              Checks your minecoin balance.", colour=discord.Color.orange(), url="")
    embed.set_footer(text="Made By Senpai Satan#6969", icon_url="https://cdn.discordapp.com/attachments/606173754258882560/614419385049808896/unknown.png")
    await ctx.send(embed=embed)

@bot.command()
async def mines(ctx):
    embed=discord.Embed(title="Mines:", description="", colour=discord.Color.orange(), url="")
    embed.add_field(name="----------", value="<:dirt:614479214967783450> Dirt:     Lvl 1")
    embed.add_field(name="----------", value="<:stone:614479264393461780> Stone:    Lvl 3")
    embed.add_field(name="----------", value="<:coal:614479289525600275> Coal:     Lvl 5")
    embed.add_field(name="----------", value="<:gold:614479398510264330> Gold:     Lvl 10")
    embed.add_field(name="----------", value="<:iron:614479445377679380> Iron:     Lvl 15")
    embed.add_field(name="----------", value="<:lapis:614479424645234690> Lapis:    Lvl 20")
    embed.add_field(name="----------", value="<:redstone:614480910502330368> Redstone: lvl 30")
    embed.add_field(name="----------", value="<:diamond:614480931612393476> Diamond:  Lvl 40")
    embed.add_field(name="----------", value="<:emerald:614480949752758305> Emerald:  Lvl 50")
    embed.add_field(name="----------", value="<:bedrock:614480966844678151> Bedrock:  Lvl 100")
    await ctx.send(embed=embed)

@bot.command()
async def check(ctx, *, arg):
    if arg == "dirt":
        embed=discord.Embed(title="Dirt Mine:", description="<:dirt:614479214967783450> 99%\n\n<:stone:614479264393461780> 1%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "stone":
        embed=discord.Embed(title="Stone Mine:", description="<:dirt:614479214967783450> 75%\n\n<:stone:614479264393461780> 23%\n\n<:coal:614479289525600275> 2%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "coal":
        embed=discord.Embed(title="Coal Mine:", description="<:dirt:614479214967783450> 25%\n\n<:stone:614479264393461780> 50%\n\n<:coal:614479289525600275> 23%\n\n<:gold:614479398510264330> 2%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "gold":
        embed=discord.Embed(title="Gold Mine:", description="<:dirt:614479214967783450> 20%\n\n<:stone:614479264393461780> 40%\n\n<:coal:614479289525600275> 30%\n\n<:gold:614479398510264330> 10%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "iron":
        embed=discord.Embed(title="Iron Mine:", description="<:dirt:614479214967783450> 10%\n\n<:stone:614479264393461780> 20%\n\n<:coal:614479289525600275> 20%\n\n<:gold:614479398510264330> 20%\n\n<:iron:614479445377679380> 20%\n\n<:lapis:614479424645234690> 10%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "lapis":
        embed=discord.Embed(title="Lapis Mine:", description="<:dirt:614479214967783450> 5%\n\n<:stone:614479264393461780> 10%\n\n<:coal:614479289525600275> 10%\n\n<:gold:614479398510264330> 10%\n\n<:iron:614479445377679380> 10%\n\n<:lapis:614479424645234690> 10%\n\n<:redstone:614480910502330368> 20%\n\n<:diamond:614480931612393476> 15%\n\n<:emerald:614480949752758305> 9%\n\n<:bedrock:614480966844678151> 1%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "redstone":
        embed=discord.Embed(title="Redstone Mine:", description="<:dirt:614479214967783450> 5%\n\n<:stone:614479264393461780> 5%\n\n<:coal:614479289525600275> 10%\n\n<:gold:614479398510264330> 10%\n\n<:iron:614479445377679380> 10%\n\n<:lapis:614479424645234690> 10%\n\n<:redstone:614480910502330368> 20%\n\n<:diamond:614480931612393476> 20%\n\n<:emerald:614480949752758305> 5%\n\n<:bedrock:614480966844678151> 5%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "diamond":
        embed=discord.Embed(title="Diamond Mine:", description="<:stone:614479264393461780> 1%\n\n<:coal:614479289525600275> 5%\n\n<:gold:614479398510264330> 5%\n\n<:iron:614479445377679380> 9%\n\n<:lapis:614479424645234690> 10%\n\n<:redstone:614480910502330368> 10%\n\n<:diamond:614480931612393476> 20%\n\n<:emerald:614480949752758305> 20%\n\n<:bedrock:614480966844678151> 20%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "emerald":
        embed=discord.Embed(title="Emerald Mine:", description="<:iron:614479445377679380> 5%\n\n<:lapis:614479424645234690> 5%\n\n<:redstone:614480910502330368> 10%\n\n<:diamond:614480931612393476> 20%\n\n<:emerald:614480949752758305> 30%\n\n<:bedrock:614480966844678151> 30%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    elif arg == "bedrock":
        embed=discord.Embed(title="Bedrock Mine:", description="<:lapis:614479424645234690> 5%\n\n<:redstone:614480910502330368> 5%\n\n<:diamond:614480931612393476> 10%\n\n<:emerald:614480949752758305> 20%\n\n<:bedrock:614480966844678151> 60%", colour=discord.Color.orange(), url="")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid mine name.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)

@bot.command()
async def inventory(ctx):
    embed=discord.Embed(title="Inventory:", description="", colour=discord.Color.orange(), url="")
    if dirt > 0:
        embed.add_field(name="----------", value=f"<:dirt:614479214967783450> {dirt}", inline=False)
    if stone > 0:
        embed.add_field(name="----------", value=f"<:stone:614479264393461780> {stone}", inline=False)
    if coal > 0:
        embed.add_field(name="----------", value=f"<:coal:614479289525600275> {coal}", inline=False)
    if gold > 0:
        embed.add_field(name="----------", value=f"<:gold:614479398510264330> {gold}", inline=False)
    if iron > 0:
        embed.add_field(name="----------", value=f"<:iron:614479445377679380> {iron}", inline=False)
    if lapiz > 0:
        embed.add_field(name="----------", value=f"<:lapis:614479424645234690> {lapiz}", inline=False)
    if redstone > 0:
        embed.add_field(name="----------", value=f"<:redstone:614480910502330368> {redstone}", inline=False)
    if diamond > 0:
        embed.add_field(name="----------", value=f"<:diamond:614480931612393476> {diamond}", inline=False)
    if emerald > 0:
        embed.add_field(name="----------", value=f"<:emerald:614480949752758305> {emerald}", inline=False)
    if bedrock > 0:
        embed.add_field(name="----------", value=f"<:bedrock:614480966844678151> {bedrock}", inline=False)
    if dirt == 0 and stone == 0 and coal == 0 and gold == 0 and iron == 0 and lapiz == 0 and redstone == 0 and diamond == 0 and emerald == 0 and bedrock == 0:
        embed=discord.Embed(title="You have no items in your inventory.", description="", colour=discord.Color.yellow(), url="")
    await ctx.send(embed=embed)

@bot.command()
async def switch(ctx, *, arg):
    embed=discord.Embed(title=f"Successfully switched to {arg} mine.", description="", colour=discord.Color.blue(), url="")
    if arg == "dirt":
        await ctx.send(embed=embed)
        global m
        m = "dirt"
    elif arg == "stone":
        if l >= 3:
            await ctx.send(embed=embed)
            m = "stone"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "coal":
        if l >= 5:
            await ctx.send(embed=embed)
            m = "coal"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "gold":
        if l >= 10:
            await ctx.send(embed=embed)
            m = "gold"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "iron":
        if l >= 15:
            await ctx.send(embed=embed)
            m = "iron"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "lapis":
        if l >= 20:
            await ctx.send(embed=embed)
            m = "lapiz"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "redstone":
        if l >= 30:
            await ctx.send(embed=embed)
            m = "redstone"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "diamond":
        if l >= 40:
            await ctx.send(embed=embed)
            m = "diamond"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "emerald":
        if l >= 50:
            await ctx.send(embed=embed)
            m = "emerald"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "bedrock":
        if lvl == 100:
            await ctx.send(embed=embed)
            m = "bedrock"
        else:
            embed=discord.Embed(title="You're not high enough lvl for that.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid mine name.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)

@bot.command()
async def lvl(ctx):
    embed=discord.Embed(title=f"You are lvl {l}.", description="", colour=discord.Color.orange(), url="")
    await ctx.send(embed=embed)

@bot.command()
async def balance(ctx):
    embed=discord.Embed(title=f"You have {minecoins} minecoins.", description="", colour=discord.Color.orange(), url="")
    await ctx.send(embed=embed)

@bot.command()
async def shop(ctx):
    embed=discord.Embed(title="Shop:", description="<:woodpick:614668980652736523> wooden pick:   (50 minecoins)   (1 block)\n\n<:stonepick:614668966782304274> stone pick:    (200 minecoins)  (2 blocks)\n\n<:goldpick:614668907894013962> gold pick:     (500 minecoins)  (3 blocks)\n\n<:ironpick:614668948956512263> iron pick:     (2000 minecoins) (4 blocks)\n\n<:diamondpick:614668885504950293> diamond pick:  (5000 minecoins) (5 blocks)", colour=discord.Color.orange(), url="")
    embed.set_footer(text=f"{minecoins}", icon_url="https://cdn.discordapp.com/attachments/606173754258882560/614747368062976021/minecoin.png")
    await ctx.send(embed=embed)

@bot.command()
async def buy(ctx, *, arg):
    if arg == "wooden pick":
        global woodp
        if woodp == 0:
            global minecoins
            if minecoins >= 50:
                minecoins = minecoins-50
                woodp = 1
                embed=discord.Embed(title="Successfully purchased the wooden pick for 50 minecoins.", description="", colour=discord.Color.blue(), url="")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="You don't have enough minecoins to purchase that item.", description="", colour=discord.Color.red(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You allready own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "stone pick":
        global stonep
        if stonep == 0:
            if minecoins >= 200:
                minecoins = minecoins-200
                stonep = 1
                embed=discord.Embed(title="Successfully purchased the stone pick for 200 minecoins.", description="", colour=discord.Color.blue(), url="")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="You don't have enough minecoins to purchase that item.", description="", colour=discord.Color.red(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You allready own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "gold pick":
        global goldp
        if goldp == 0:
            if minecoins >= 500:
                minecoins = minecoins-500
                goldp = 1
                embed=discord.Embed(title="Successfully purchased the gold pick for 500 minecoins.", description="", colour=discord.Color.blue(), url="")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="You don't have enough minecoins to purchase that item.", description="", colour=discord.Color.red(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You allready own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "iron pick":
        global ironp
        if ironp == 0:
            if minecoins >= 2000:
                minecoins = minecoins-2000
                ironp = 1
                embed=discord.Embed(title="Successfully purchased the iron pick for 2000 minecoins.", description="", colour=discord.Color.blue(), url="")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="You don't have enough minecoins to purchase that item.", description="", colour=discord.Color.red(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You allready own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "diamond pick":
        global diamondp
        if diamondp == 0:
            if minecoins >= 5000:
                minecoins = minecoins-5000
                diamondp = 1
                embed=discord.Embed(title="Successfully purchased the diamond pick for 5000 minecoins.", description="", colour=discord.Color.blue(), url="")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="You don't have enough minecoins to purchase that item.", description="", colour=discord.Color.red(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You allready own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid item name.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)

@bot.command()
async def equip(ctx, *, arg):
    embed=discord.Embed(title=f"Successfully equipped {arg}.", description="", colour=discord.Color.orange(), url="")
    if arg == "wooden pick":
        if woodp == 1:
            global pick
            if pick != 1:
                pick = 1
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f"{arg} is allready equiped.", description="", colour=discord.Color.orange(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You don't own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "stone pick":
        if stonep == 1:
            if pick != 2:
                pick = 2
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f"{arg} is allready equiped.", description="", colour=discord.Color.orange(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You don't own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "gold pick":
        if goldp == 1:
            if pick != 3:
                pick = 3
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f"{arg} is allready equiped.", description="", colour=discord.Color.orange(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You don't own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "iron pick":
        if ironp == 1:
            if pick != 4:
                pick = 4
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f"{arg} is allready equiped.", description="", colour=discord.Color.orange(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You don't own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "diamond pick":
        if diamondp == 1:
            if pick != 5:
                pick = 5
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f"{arg} is allready equiped.", description="", colour=discord.Color.orange(), url="")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="You don't own that item.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid item name.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)

@bot.command()
async def sell(ctx, *, arg):
    if arg == "dirt":
        global sel
        global dirt
        sel = dirt
        dirt = 0
        global minecoins
        minecoins = minecoins+sel
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:dirt:614479214967783450> {sel} (<:minecoin:614725810791776258>{sel})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:dirt:614479214967783450> {sel} (<:minecoin:614725810791776258>{sel})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} blocks to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "stone":
        global stone
        sel = stone
        stone = 0
        minecoins = minecoins+sel*2
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:stone:614479264393461780> {sel} (<:minecoin:614725810791776258>{sel*2})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:stone:614479264393461780> {sel} (<:minecoin:614725810791776258>{sel*2})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} blocks to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)

    elif arg == "coal":
        global coal
        sel = coal
        coal = 0
        minecoins = minecoins+sel*3
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:coal:614479289525600275> {sel} (<:minecoin:614725810791776258>{sel*3})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:coal:614479289525600275> {sel} (<:minecoin:614725810791776258>{sel*3})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "gold":
        global gold
        sel = gold
        gold = 0
        minecoins = minecoins+sel*5
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:gold:614479398510264330> {sel} (<:minecoin:614725810791776258>{sel*5})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:gold:614479398510264330> {sel} (<:minecoin:614725810791776258>{sel*5})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "iron":
        global iron
        sel = iron
        iron = 0
        minecoins = minecoins+sel*10
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:iron:614479445377679380> {sel} (<:minecoin:614725810791776258>{sel*10})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:iron:614479445377679380> {sel} (<:minecoin:614725810791776258>{sel*10})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "lapiz":
        global lapiz
        sel = lapiz
        lapiz = 0
        minecoins = minecoins+sel*20
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:lapis:614479424645234690> {sel} (<:minecoin:614725810791776258>{sel*20})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:lapis:614479424645234690> {sel} (<:minecoin:614725810791776258>{sel*20})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "redstone":
        global redstone
        sel = redstone
        redstone = 0
        minecoins = minecoins+sel*30
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:redstone:614480910502330368> {sel} (<:minecoin:614725810791776258>{sel*30})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:redstone:614480910502330368> {sel} (<:minecoin:614725810791776258>{sel*30})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "diamond":
        global diamond
        sel = diamond
        diamond = 0
        minecoins = minecoins+sel*40
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:diamond:614480931612393476> {sel} (<:minecoin:614725810791776258>{sel*40})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:diamond:614480931612393476> {sel} (<:minecoin:614725810791776258>{sel*40})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg}s to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "emerald":
        global emerald
        sel = emerald
        emerald = 0
        minecoins = minecoins+sel*50
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:emerald:614480949752758305> {sel} (<:minecoin:614725810791776258>{sel*50})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:emerald:614480949752758305> {sel} (<:minecoin:614725810791776258>{sel*50})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg}s to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "bedrock":
        global bedrock
        sel = bedrock
        bedrock = 0
        minecoins = minecoins+sel*100
        if sel > 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:bedrock:614480966844678151> {sel} (<:minecoin:614725810791776258>{sel*100})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        elif sel == 1:
            embed=discord.Embed(title=f"Successfully Sold:", description=f"<:bedrock:614480966844678151> {sel} (<:minecoin:614725810791776258>{sel*100})", colour=discord.Color.blue(), url="")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"You don't have any {arg} to sell.", description="", colour=discord.Color.red(), url="")
            await ctx.send(embed=embed)
    elif arg == "all":
        global tsel
        embed=discord.Embed(title="Successfully Sold:", description="", colour=discord.Color.blue(), url="")
        if dirt > 0:
            global tl
            tl = tl+1
            sel = dirt
            tsel = sel
            dirt = 0
            minecoins = minecoins+sel
            embed.add_field(name="----------", value=f"<:dirt:614479214967783450> {sel} (<:minecoin:614725810791776258>{sel})", inline=False)
        if stone > 0:
            tl = tl+1
            sel = stone
            tsel = tsel+sel*2
            stone = 0
            minecoins = minecoins+sel*2
            embed.add_field(name="----------", value=f"<:stone:614479264393461780> {sel} (<:minecoin:614725810791776258>{sel*2})", inline=False)
        if coal > 0:
            tl = tl+1
            sel = coal
            tsel = tsel+sel*3
            coal = 0
            minecoins = minecoins+sel*3
            embed.add_field(name="----------", value=f"<:coal:614479289525600275> {sel} (<:minecoin:614725810791776258>{sel*3})", inline=False)
        if gold > 0:
            tl = tl+1
            sel = gold
            tsel = tsel+sel*5
            gold = 0
            minecoins = minecoins+sel*5
            embed.add_field(name="----------", value=f"<:gold:614479398510264330> {sel} (<:minecoin:614725810791776258>{sel*5})", inline=False)
        if iron > 0:
            tl = tl+1
            sel = iron
            tsel = tsel+sel*10
            iron = 0
            minecoins = minecoins+sel*10
            embed.add_field(name="----------", value=f"<:iron:614479445377679380> {sel} (<:minecoin:614725810791776258>{sel*10})", inline=False)
        if lapiz > 0:
            tl = tl+1
            sel = lapiz
            tsel = tsel+sel*20
            lapiz = 0
            minecoins = minecoins+sel*20
            embed.add_field(name="----------", value=f"<:lapis:614479424645234690> {sel} (<:minecoin:614725810791776258>{sel*20})", inline=False)
        if redstone > 0:
            tl = tl+1
            sel = redstone
            tsel = tsel+sel*30
            redstone = 0
            minecoins = minecoins+sel*30
            embed.add_field(name="----------", value=f"<:redstone:614480910502330368> {sel} (<:minecoin:614725810791776258>{sel*30})", inline=False)
        if diamond > 0:
            tl = tl+1
            sel = diamond
            tsel = tsel+sel*40
            diamond = 0
            minecoins = minecoins+sel*40
            embed.add_field(name="----------", value=f"<:diamond:614480931612393476> {sel} (<:minecoin:614725810791776258>{sel*40})", inline=False)
        if emerald > 0:
            tl = tl+1
            sel = emerald
            tsel = tsel+sel*50
            emerald = 0
            minecoins = minecoins+sel*50
            embed.add_field(name="----------", value=f"<:emerald:614480949752758305> {sel} (<:minecoin:614725810791776258>{sel*50})", inline=False)
        if bedrock > 0:
            tl = tl+1
            sel = bedrock
            tsel = tsel+sel*100
            bedrock = 0
            minecoins = minecoins+sel*100
            embed.add_field(name="----------", value=f"<:bedrock:614480966844678151> {sel} (<:minecoin:614725810791776258>{sel*100})", inline=False)
        if tl > 1:
            embed.add_field(name="----------", value=f"Total: <:minecoin:614725810791776258>{tsel}")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid block name.", description="", colour=discord.Color.red(), url="")
        await ctx.send(embed=embed)

bot.run("NTU2OTU0NDExMDkyNDEwMzY5.XV4Kuw.JmE72xq_EOjMA87woHKjo-I9N1o", bot=False)

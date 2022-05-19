import discord
import random
import time
import requests
from discord.ext import commands
from discord.ext import tasks
#client是我們與Discord連結的橋樑
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)





#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
	print('目前登入身份：',client.user)
	game = discord.Game('指令"!你會幹嘛"查看功能')
	#這邊設定機器當前的狀態文字
	#discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
	await client.change_presence(status=discord.Status.online, activity=game)
	global Is_Notificated
	Is_Notificated = False
	
	
	#embed=discord.Embed(title="看完點擊下方【"+'<:fox:887613110326816850>'+"】領取生菜身分組", color=0xe999ff)
	#cha = client.get_channel(887618038390734870)
	#m = await cha.send(embed=embed)
	#await m.add_reaction('<:fox:887613110326816850>')
 
    
@client.event
#當有訊息時
async def on_message(message):
	#排除自己的訊息，避免陷入無限循環
	if message.author == client.user:
		return


	#如果以「說」開頭
	if message.content.startswith('說') and f'{type(message.channel)}' == "<class 'discord.channel.DMChannel'>":
		if f'{message.channel.recipient}' == '玥玥ㄚ#7445':
			# 說 [channelID] [text]
			print(message)
			user_input = message.content.split(" ")
			if len(user_input) == 3:
				cha = client.get_channel(int(user_input[1]))
				await cha.send(user_input[2])
	if f'{type(message.channel)}' == "<class 'discord.channel.DMChannel'>":
		print(f'{message.channel.recipient}'+'私訊：'+message.content)
	if message.content.startswith('說'):
		tmp = message.content.split(" ",2)
		print(f'{message.author}'+'used 說')
		if len(tmp) == 1:
			await message.channel.send("你要我說什麼啦？")
		else:
			await message.channel.send(f"{message.author.mention}逼我說："+tmp[1])

			
		
	if message.content == '嗨':
		await message.channel.send(f"{message.author.mention} 你好呀")
		print(f'{message.author}'+'used 嗨')
	if message.content == '早安':
		await message.channel.send(f"{message.author.mention} 早呀")
		print(f'{message.author}'+'used 早安')
	if message.content == '玥玥怎麼樣':
		await message.channel.send("玥玥很棒人好又溫柔可愛呀")
		print(f'{message.author}'+'used 玥玥怎麼樣')
	if message.content.startswith('!抽籤'):
		draw=["大吉","小吉","中","小凶","大凶"]
		tmp = message.content.split(" ",2)
		print(f'{message.author}'+'used 抽籤')
		if len(tmp) == 1:
			await message.channel.send(f"{message.author.mention} 你算什麼東西？我是說，你要算什麼東西？")
		else:
			dn = random.randint(0,4)
			d = draw[dn]
			Pickdn = ""
			if dn==0:
				Pickdn = f"是「{d}」喔喔喔！！！✧｡٩(ˊᗜˋ)و✧*｡"
			elif dn==1:
				Pickdn = f"是「{d}」喔喔喔！！！✧｡٩(ˊᗜˋ)و✧*｡"
			elif dn==2:
				Pickdn = f"是「{d}」喔，平平淡淡不好不壞v(￣︶￣)y"
			elif dn==3:
				Pickdn = f"是「{d}」喔(´･ω･`)"
			elif dn==4:
				Pickdn = f"(⊙０⊙)是「{d}」喔，拍拍你 (´･_･`)"			
			embed_sign=discord.Embed(title="問："+tmp[1], description=Pickdn, color=0xff9ecd)
			embed_sign.set_author(name=message.author.name, icon_url=message.author.avatar_url)
			await message.channel.send(embed=embed_sign)

	#你會幹嘛
	if message.content.startswith('!你會幹嘛'):
		print(f'{message.author}'+'used !你會幹嘛')
		#embed=discord.Embed(title="我會的不多啦", description="我會發玥玥的開台通知和給生菜的身分組", color=0x8fb4ff)
		#embed.add_field(name="嗨",value="我會對你嗨", inline=True)
		#embed.add_field(name="早安",value="我會對你說早安", inline=True)
		#embed.add_field(name="玥玥怎麼樣",value="我會告訴你玥玥怎麼樣", inline=True)
		#embed.add_field(name="!你會幹嘛", value="查看指令", inline=True)
		#embed.add_field(name="說[空格][文字]", value="記得空格加要我說的話", inline=True)
		#embed.add_field(name="!抽籤[空格][文字]", value="記得空格加想問什麼", inline=True)
		#embed.set_footer(text="generated by 玥玥")
		#await message.channel.send(embed=embed)
		await message.channel.send("```python"+'\n'
						+"我會的不多...QAQ"+'\n'
						+"我會發玥玥的開台通知和給生菜的身分組"+'\n'
						+'\n'
						+"- 嗨 #我會對你嗨"+'\n'
						+"- 早安 #我會對你說早安"+'\n'
						+"- 玥玥怎麼樣"+'\n'
						+"- !你會幹嘛 #查看指令"+'\n'
						+"- 說[空格][文字] #沒打文字我會不爽，沒空格我不會理你"+'\n'
						+"- !抽籤[空格][文字] #沒打文字我會罵你喔，沒空格我不會理你"+'\n'
						+"```")

with open("nono.neddih","r",encoding="utf-8") as f:
	not_token = f.read()

client.run(not_token)
from certifi import contents
import discord
import random
import time
import requests
import datetime
import json
from discord_components import Button, ButtonStyle, DiscordComponents, ComponentsBot
from discord.ext import commands
from discord.ext import tasks
#client是我們與Discord連結的橋樑
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
DiscordComponents(client)





#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
	print('目前登入身份：',client.user)
	game = discord.Game('"!你會幹嘛"查看功能')
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
		if f'{message.channel.recipient}' == 'Sugarrr#6130':
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
	if message.content == '!get':
		print(f'{message.author}'+'author')
		print(f'{message.author.id}'+'id')
		print(f'{message.author.name}'+'name')
		print(f'{message.author.display_name}'+'displayname')
		print(f'{client.user}'+'clientuser')
		print(f'{client.user.avatar_url}'+'clientuseravatarurl')		
		
	
	if message.content == '!test':
		components = [
			[Button(label='剪刀',
                                   custom_id='op1',
                                   emoji="✂️",
                                   style=ButtonStyle.green),
                            Button(label='石頭',
                                   custom_id='op2',
                                   emoji="✊",
                                   style=ButtonStyle.grey),
							Button(label='布',
                                   custom_id='op3',
                                   emoji="🧻",
                                   style=ButtonStyle.blue)]]
		w_del = await message.channel.send("入場費200，猜贏得500，平手退100",components=components)
		dn = (random.randint(0,8))


		with open("user_data.json",'r') as f:
			file2 = json.loads(f.read())
			check_id = 0
			m = 0
			for i in range(len(file2["user"])):
				j = file2["user"][i]
				if j.get("id") == f'{message.author.id}':
					check_id = 1
					interaction = await client.wait_for("button_click")
					if interaction.component.label == '剪刀':
						if dn == 0:
							str1 = "我出石頭啦嫩"
							m = -200
						elif dn == 1:
							str1 = "我出剪刀，真有默契"
							m = 100
						elif dn == 2:
							str1 = "我出布，喔不"
							m = 500
					if interaction.component.label == '石頭':
						if dn == 0:
							str1 = "我出石頭，真有默契"
							m = 100
						elif dn == 1:
							str1 = "我出剪刀，喔不"
							m = 500
						elif dn == 2:
							str1 = "我出布啦嫩"
							m = -200
					if interaction.component.label == '布':
						if dn == 0:
							str1 = "我出石頭，喔不"
							m = 500
						elif dn == 1:
							str1 = "我出剪刀啦嫩"
							m = -200
						elif dn == 2:
							str1 = "我出布，真有默契"
							m = 100

					a_money = j["money"] + m
					j["money"] += m
					embed=discord.Embed(title=str1, description=f"目前擁有 {a_money}", color=0xffdd00)
					embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
					embed.set_footer(text="入場費200，猜贏得500，平手退100")
					await message.channel.send(embed=embed)
					await w_del.delete()
					with open("user_data.json",'w') as f:
						file2 = json.dumps(file2)
						f.write(file2)
						f.close()
					break

			if check_id == 0:
				await message.channel.send(f"{message.author.mention}你還沒報到，輸入'!報到'報到")
			f.close()

#rank
	if message.content == '!rank':

		#Read json
		with open("user_data.json",'r', encoding='utf-8') as f:
			file2 = json.loads(f.read())
			list_of_i = [(0,'0'),(0,'0'),(0,'0'),(0,'0'),(0,'0'),(0,'0'),(0,'0')]
			for i in range(len(file2["user"])):
				j = file2["user"][i]
				list_of_i.sort(key = lambda s :s[0], reverse = True)
				for k in range(7):
					compare_money = list_of_i[k][0]
					if j.get("money") > compare_money :
						list_of_i.insert(k,(j.get("money"),j.get("name+num")))
						del(list_of_i[-1])
						break
			print(list_of_i)
			f.close()
		embed=discord.Embed(title="土豪們", description="`沒上榜請再接再厲><`", color=0xff0000)
		embed.add_field(name="No.",value="1."+'\n'+"2."+'\n'+"3."+'\n'+"4."+'\n'+"5."+'\n'+"6."+'\n'+"7.", inline=True)
		embed.add_field(name="id",value=list_of_i[0][1]+'\n'+list_of_i[1][1]+'\n'+list_of_i[2][1]+'\n'+list_of_i[3][1]+'\n'+list_of_i[4][1]+'\n'+list_of_i[5][1]+'\n'+list_of_i[6][1], inline=True)
		embed.add_field(name="money",value=str(list_of_i[0][0])+'\n'+str(list_of_i[1][0])+'\n'+str(list_of_i[2][0])+'\n'+str(list_of_i[3][0])+'\n'+str(list_of_i[4][0])+'\n'+str(list_of_i[5][0])+'\n'+str(list_of_i[6][0]), inline=True)
		await message.channel.send(embed=embed)

		
	#簽到抽卡
	#簽
	if message.content == '!簽':
		sign_date = str(datetime.date.today())

		#Read json
		with open("user_data.json",'r') as f:
			file2 = json.loads(f.read())
			check_id = 0
			for i in range(len(file2["user"])):
				j = file2["user"][i]
				if j.get("id") == f'{message.author.id}':
					check_id = 1
					j["name"] = f'{message.author.name}'
					j["name+num"] = f'{message.author}'
					if j.get("date") == sign_date:
						await message.channel.send(f"{message.author.mention}你今天簽到過了喔")
					else:
						#抽
						lottery = "abbbcccccccccccccccc"
						count_money = 0
						count_pic = ""

						for i in range(10):
							dn = random.randint(0,19)
							Ldn = lottery[dn]
							if Ldn == "a":
								count_money += 1000
								count_pic += '<:wow_1000:977904107744530512> '
							if Ldn == "b":
								count_money += 250
								count_pic += '<:wow_250:977905164843360256> '
							if Ldn == "c":
								count_money += 50
								count_pic += '<:wow_50:977905164604297236> '

						a_money = j["money"] + count_money
						embed=discord.Embed(title="簽到成功", description=f"獲得 {count_money}，目前擁有 {a_money}", color=0xffdd00)
						embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
						embed.set_footer(text="非猷 80% | 小運氣 15% | 歐皇 5%")
						await message.channel.send(embed=embed)
						await message.channel.send(count_pic)


						j["date"]=sign_date
						j["money"] += count_money
						with open("user_data.json",'w') as f:
							file2 = json.dumps(file2)
							f.write(file2)
							f.close()
						break

			if check_id == 0:
				await message.channel.send(f"{message.author.mention}你還沒報到，輸入'!報到'報到")
			f.close()

	


	if message.content == '!報到':

	#取user資料
		user_data = {"id": f'{message.author.id}',"Name": f'{message.author.name}',"name+num":f'{message.author}',"money": 1000,"date":""}	
		#Read json
		with open("user_data.json",'r') as f:
			file2 = json.loads(f.read())
			check_id = 0
			for i in file2["user"]:
				if i.get("id") == f'{message.author.id}':
					check_id = 1
					await message.channel.send(f"{message.author.mention}你已經報到過了喔")

			if check_id == 0:
				await message.channel.send(f"{message.author.mention}報到成功，獲得1000")
				file2["user"].append(user_data)
				
			f.close()
		
		with open("user_data.json",'w') as f:
			file2 = json.dumps(file2)
			f.write(file2)
			f.close()

	if message.content.startswith('!賭'):
		tmp = message.content.split(" ",2)
		if (tmp[1] != "藍" and tmp[1] != "紅") or tmp[2].isdigit()==False or len(tmp)!=3:
			await message.channel.send(f"{message.author.mention}格式輸入錯誤 ex.`!賭 藍 100`")
		elif int(tmp[2])<0:
				await message.channel.send(f"{message.author.mention}別想騙我(σﾟ∀ﾟ)σ")
		else:
			if tmp[1]=="藍":
				g = 0
			elif tmp[1]=="紅":
				g = 1

			with open("user_data.json",'r') as f:
				file2 = json.loads(f.read())
				check_id = 0
				for i in range(len(file2["user"])):
					j = file2["user"][i]
					if j.get("id") == f'{message.author.id}':
						if j.get("money") < int(tmp[2]):
							await message.channel.send("窮鬼，滾OvO")
							break
						check_id = 1

						#黑紅隨機
						draw = ["🟦","🟥"]
						dn = random.randint(0,1)
						if g == dn:
							m = int(tmp[2])
							m = m*2
							a_money = j["money"] + m
							j["money"] += m
							embed=discord.Embed(title="結果", description=f"獲得 {int(tmp[2])}x2", color=0x00e658)
							embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
							embed.add_field(name="顏色是",value=draw[dn], inline=True)
							embed.add_field(name="目前擁有",value=f"{a_money}", inline=True)
							await message.channel.send(embed=embed)
						else:
							m = int(tmp[2])
							a_money = j["money"] - m
							j["money"] -= m
						
							if j["money"] < 0:
								j["money"] =  0
								a_money = 0
							embed=discord.Embed(title="結果", description=f"獲得 {int(tmp[2])}x0", color=0x949494)
							embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
							embed.add_field(name="顏色是",value=draw[dn], inline=True)
							embed.add_field(name="目前擁有",value=f"{a_money}", inline=True)
							await message.channel.send(embed=embed)



						with open("user_data.json",'w') as f:
							file2 = json.dumps(file2)
							f.write(file2)
							f.close()
						break

				if check_id == 0:
					await message.channel.send(f"{message.author.mention}你還沒報到，輸入'!報到'報到")
				f.close()

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
			embed=discord.Embed(title="問："+tmp[1], description=Pickdn, color=0xff9ecd)
			embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
			await message.channel.send(embed=embed)

	#你會幹嘛
	if message.content.startswith('!你會幹嘛'):
		print(f'{message.author}'+'used !你會幹嘛')
		embed=discord.Embed(color=0x8fb4ff)
		embed.set_author(name="我會...", icon_url=client.user.avatar_url)	
		embed.add_field(name="⛦玥玥台",value="⠀開台通知&給生菜身分組", inline=True)
		embed.add_field(name="⛦文字互動",value="⠀`嗨` -> 我會對你說嗨"+'\n'+"⠀`早安` -> 我會對你說早安"+'\n'+"⠀`玥玥怎麼樣` -> 我會告訴你玥玥怎麼樣"+'\n'+"⠀`說[空格][文字]` -> 逼我說...", inline=False)
		embed.add_field(name="⛦玩的東東",value="⠀`!抽籤[空格][想問的事情]` -> 抽支吉凶籤", inline=False)
		embed.add_field(name="⛦隱藏功能",value="⠀都說是隱藏功能了", inline=False)
		#embed.add_field(name="嗨",value="我會對你嗨", inline=True)
		#embed.add_field(name="早安",value="我會對你說早安", inline=True)
		#embed.add_field(name="玥玥怎麼樣",value="我會告訴你玥玥怎麼樣", inline=True)
		#embed.add_field(name="!你會幹嘛", value="查看指令", inline=True)
		#embed.add_field(name="說[空格][文字]", value="空格加要我說的話", inline=True)
		#embed.add_field(name="!抽籤[空格][文字]", value="記得空格加想問什麼", inline=True)
		embed.set_footer(text="新玩法製作中！")
		await message.channel.send(embed=embed)
		"""
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
		"""





with open("nono.neddih","r",encoding="utf-8") as f:
	not_token = f.read()

client.run(not_token)
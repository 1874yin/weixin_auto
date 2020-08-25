from wxpy import *



bot = Bot(cache_path=True, console_qr=2)

bot.enable_puid()

f = open('friends.txt', 'w', encoding='utf-8')

f.write('昵称\t\t\t微信号\t微信ID\t备注\t性别\t城市\t签名\n')

# 获取好友列表
friends = bot.friends()

# 循环打印每个好友信息
for friend in friends:
	# 昵称
	name = friend.nick_name
	# 微信号/名称
	alias = friend.alias
	# 微信 ID 
	# wxid = friend.wxid
	wxid = friend.puid
	# 备注
	remark_name = friend.remark_name
	# 性别
	if friend.sex == 1:
		sex = '男'
	elif friend.sex == 2:
		sex = '女'
	else:
		sex = '无'
	# 城市
	city = friend.city
	# 签名
	signature = friend.signature

	# print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (name, alias, wxid, remark_name, sex, city, signature))
	f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (name, alias, wxid, remark_name, sex, city, signature))

if f:
	f.close()

friends_stat = friends.stats_text()
print(friends_stat)
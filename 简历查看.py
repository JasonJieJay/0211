#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test
while 1:
	print('''
	查看已经录入的简历信息：
	输入a，按照名字进行查询
	输入b，按照电话进行查询
	输入c, 按照经历进行查询
	输入q, 退出程序
	''')

	shuru=input('请输入您的选择: ')
	if shuru=='a':
		name2=input('请输入您查询的名字')
		data=db.jianli.find({'name':name2},{'_id':0})
		for i in data:
			print('名字：'+i['name']+' 电话 '+i['tel'])
	elif shuru=='b':
		name3=input('请输入您查询的电话')
		data=db.jianli.find({'tel':name3},{'_id':0})
		for i in data:
			print('名字：'+i['name']+' 电话 '+i['tel'])
	elif shuru=='c':
		name4=input('请输入您查询的经历')
		data=db.jianli.find({'ex':name4},{'_id':0})
		for i in data:
			print('名字：'+i['name']+' 电话 '+i['tel'])
	elif shuru=='q':
		print('已退出')
		break
	else:
		print('您的输入有误！')





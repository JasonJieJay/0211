#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test
#输入：名字  电话   经历
while 1:
	name=input('请输入您的名字：')
	tel=input('请输入您的电话：')
	ex=input('请输入您的工作经历:')
	su=input('确信信息无误输入yes')

	if su=='yes':
		db.jianli.insert({'name':name,'tel':tel,'ex':ex})
		print('OK')
		#continue
	elif su=='quit':
		break
	else:
		print('请重新输入信息')
#新增一个文档进行测试
#db.jianli.insert({'name':name,'tel':tel,'ex':ex})
#print('ok')

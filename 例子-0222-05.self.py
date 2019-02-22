#coding=utf-8
class student:
	def __init__(self,name):
		self.name=name
	def info(self):
		print('你的名字是%s'%self.name)

def studentinfo(s):
	s.info()

heygor=student('ladygaga')
#heygor是student类的实例化对象
#对象实例化后可以使用类的方法
studentinfo(heygor)

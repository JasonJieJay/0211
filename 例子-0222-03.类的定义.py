#coding=utf-8
class student:
	def study(self):
		print('im study!')
	def play(self):
		print('play ball')
boy=student()
#产生一个student对象，通过boy实例对象来访问属性和方法
boy.age=20
#给对象添加属性，注意：后面再次出现，表示对属性进行修改
boy.favor='football'

boy.study()
boy.play()
#通过实例对象访问类的方法

print(boy.age)
print(boy.favor)



#coding=utf-8
#嵌套函数
'''
def t1():
	print('im t1!')

def t2():
	t1()
	print('im t2')

def t3():
	t2()
	print('im t3')

t3()

'''
#例子:阶乘   n!=1*2*3*.....

def func(n):
	if n==1:
		return n
	elif n>1:
		return n*func(n-1)
	else:
		return '请传递大于0的参数'

print(func(5))
#相当于5的阶乘  1*2*3*4*5=120
'''
==(5)
	==(5*func(4))
		==(4*func(3))
			...
'''

#例子：盗梦空间
def func(n):
	print('进入到%d层梦'%n)
	if n==3:
		print('进入到潜意识区')
	else:
		func(n+1)
	print('从第%d层梦中醒来'%n)

func(1)














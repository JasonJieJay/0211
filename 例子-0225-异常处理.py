#coding=utf-8
'''
try:
	p
except NameError as e:
	print('catch error!')
'''
'''

try:
	f=open('666','r')
	print(f.read())
finally:
	print('im living!')

'''

try:
	f
except NameError as e:
	print('catch error!')
finally:
	print('找不到吧！')


#coding=utf-8
'''
#计算一个函数的运行时间
import time
def jisuan(func):
	def zsq():
		starttime=time.time()
		func()
		endtime=time.time()
		sec=endtime-starttime
		print('消耗的时间为%d'%sec)
	return zsq

@jisuan
def func():
	print('hello')
	time.sleep(1)
	print('world!')

f=func
f()

'''
import time
def dec(func):
	def jisuan(a,b):
		startime=time.time()
		func(a,b)
		endtime=time.time()
		sec=endtime-startime
		print('time is %d s'%sec)
	return jisuan

@dec
def func(a,b):
	print('a+b=?')
	time.sleep(1)
	print('its',a+b)



f=func
f(4,5)






















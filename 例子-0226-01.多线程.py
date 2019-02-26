#coding=utf-8
import time
import threading
'''
import threading
print(threading.active_count())		#获取当前线程数量
print(threading.current_thread())	#查看当前运行的线程

#添加线程
def thread_job():
	print('当前线程是%s'%threading.current_thread())

def thread_job2():
	print('当前线程是%s'%threading.current_thread())

thread=threading.Thread(target=thread_job)
thread1=threading.Thread(target=thread_job2)
thread.start()
thread1.start()
'''
'''

def t1():
	print('T1开始了')
	for i in range(10):
		time.sleep(0.1)
	print('T1结束')

def t2():
	print('t2开始了')
	print('t2结束了')

th1=threading.Thread(target=t1)
th2=threading.Thread(target=t2)
th1.start()
th2.start()
th2.join()
th1.join()
print('finished')
'''
def job1():
	global A,lock
	lock.acquire()
	for i in range(10):
		A+=1
		print('job',A)
	lock.release()

def job2():
	global A,lock
	lock.acquire()
	for i in range(10):
		A+=10
		print('job2',A)
	lock.release()

lock=threading.Lock()
A=0
th1=threading.Thread(target=job1)
th2=threading.Thread(target=job2)
th1.start()
th2.start()
th2.join()
th1.join()
















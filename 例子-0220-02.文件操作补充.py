#coding=utf-8

file=open('/home/heygor/0220/txl.txt','r')
for i in file.readlines():
	#print(i)
	i=i.strip('\n')
	a=i.split(' ')
	#print(a)
	#print(type(i))
	if a[-1]=='110':
		print('tel is here!')
file.close()

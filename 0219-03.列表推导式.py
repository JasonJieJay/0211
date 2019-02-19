#coding=utf-8
#给定列表进行操作
a=[1,2,3,4]
print([5*x for x in a])
'''
b=[]
for i in a:
	b.append(i*5)
	#print(i*5)
print(b)
'''
#没有给定列表可以使用range方法
print([3*x for x in range(1,11)])

#加入if条件进行推导
print([x for x in a if x%2==0])

#多个for语句进行列表推导
print([[x,y] for x in range(2) for y in range(2)])


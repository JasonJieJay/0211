#coding=utf-8
a='hello big chui!'

print(a[0])

print(a[-2])
#print(a[30])
#切片
print(a[0:4])

print(a[:4])

print(a[4:])

print(a[3:-1])

print('*****************')
#字符串的拼接
m='simida'
n='kangsang'
print(n+m)
print(n,m)

#字符串的遍历
for i in m:
	print(i)

#成员运算
if 'i' in m:
	print('i is here')

#去空格
#strip()	取消所有空格
#lsrtip()	去掉左边空格
#rstrip()	去掉右边空格

a='      yo girl ,look at me!   '
print(a.strip())
print(a.lstrip())
print(a.rstrip())








#coding=utf-8

#直接输出

print('heygor simida!')

print(110)

#变量的输出

name='chui'

print(name)

#变量可以接受其他函数操作的结果

name=input('请输入ztl的学历：')

print(name)

#格式化输出
#    %s		替换字符类型数据，可以理解为占位
#    %d		替换数字类型数据，可以理解为占位
#    引号后面增加百分号，用于标识变量，如果有多个变量，使用小括号，标识必须和值或者变量数据类型对应
print('%s 是 o my dear mom ！'% 'chui')

print('%s 是 %d'%('python',1))

#函数输出
#abs()   判断绝对值
print(abs(-20))
print(type(name))


#补充
name=input('请输入您的帐号类型：')
print('%s的类型只能有读写权限'%name)






























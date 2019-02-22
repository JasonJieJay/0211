学习目标
掌握self的应用

课程内容
a.self实例
b.注意事项


a.self实例
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
#studentinfo括号中传入的heygor是一个已经实例化的对象，调用类里面的方法
#注意：函数传参可以传入常规函数，也可以传入对象

b.注意事项
self可以理解为自己
可以把self当作c++指针理解，就是自己
当某个对象调用其方法时候python解释器会把这个对象作为第一个参数传递给self，开发者只需要传递后面参数即可





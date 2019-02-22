
#coding=utf-8
a=10
b=20
print(a+b)
a='heygor'
b='shuai'
print(a+b)
class animal:
	def jiao(self):
		print('aowu~~~~')

class dog(animal):
	def jiao(self):
		print('gagagagaga')
class cat(animal):
	def jiao(self):
		print('eeeeeee')

def test(s):
	s.jiao()

a=animal()
a.jiao()

b=dog()
c=cat()
test(b)
test(c)















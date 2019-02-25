#coding=utf-8
'''
arr=(x for x in range(1,5))
#print(arr)
#for i in arr:
#	print(i)
print('next1 is')
print(next(arr))
print('next1 is')
print(next(arr))
print('next1 is')
print(next(arr))
'''
def test():
        n=1
        print('first!')
        yield n
        n+=1
        print('second！')
        yield n
        n+=1
        print('third')
        yield n

a=test()
print('next one is')
print(next(a))
print(next(a))

print(next(a))
print(next(a))

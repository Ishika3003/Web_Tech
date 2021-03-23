# # ishsmnt
# # list is a collection of objects of different data types
# list = []
# print(type(list))
#list = [1,'Ishika',3.9,3+4j,b'001',[1,2,3],(1,2,3),{'a':'1','b':'2'}]
# print(list[0])
# print(list[1])
# # string are immutable
# # lists are mutable 
# print(len(list))
# print(list[1])
# print(list[1][2])
# print(list[7]['b'])
# print(list[1:7:2])
# list2 = ['woo-hoo','wooh','ezra']

# list2.append('h3avren')
# print(list2)
# # raises an error
# # list2.append('ishsmnt','smnt02')
#print(dir(list))
#list.clear()


li = [1,2,3]
# li.extend([1,2,3],[1,3,4])
li.append('aws')
li.append(56)
li.append([3,4,5])

li.extend('Samant')
li.extend((1,2,5))
print(li)
# print(dir('li'))
li.extend({1:'a',2:'b',3:'c'})
print(li)
print(len(li))
print(li[13])
li.clear()
print(li)

li = [1,3,5,7]
li_2 = li.copy()
print(li_2)
li_3 = li
print(li_3)
print(li)
li_3[0]=6
print(li_3)
print(li)
print(li_2)
li = li_2.copy()
print(li)
li[0]=8
print(li)
print(li_2)
(li_2.extend([1,1,2,4,5,4,6]))
print(li_2)
print(li_2.count(2))
print(li_2.count(4))
li_2.sort()
print(li_2)
print(li_2.index(1))
print(li_2.index(4))
li_2.remove(5)
print(li_2)
li_2.pop(7)
print(li_2)

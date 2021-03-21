# ishsmnt
# list is a collection of objects of different data types
list = []
print(type(list))
list = [1,'Ishika',3.9,3+4j,b'001',[1,2,3],(1,2,3),{'a':'1','b':'2'}]
print(list[0])
print(list[1])
# string are immutable
# lists are mutable 
print(len(list))
print(list[1])
print(list[1][2])
print(list[7]['b'])
print(list[1:7:2])
list2 = ['woo-hoo','wooh','ezra']

list2.append('h3avren')
print(list2)
# raises an error
# list2.append('ishsmnt','smnt02')
# # ishsmnt
# # dictonaries are collection of  key value pairs
# i = {'a':'food','b':'clothes', 'c':'heels'}
# print(i)
# print(dir(i))
# help(i.clear)
# i.clear()
# print(i)
# dict_1 = {'one':1,'two':2,'three':3}
# print(dict_1['three'])
# # print(dict_1[3])   
# dict_1['three'] = 5
# print(dict_1) 
# print(dict_1.keys())
# print(dict_1.values())
# dict_2 = dict_1.copy()
# print(dict_2)
# dict_2['three'] = 6
# print(dict_1,dict_2)
# print(dict_1.items())
# print(dict_1.get('three'))
# print(dict_1.get('six','Ishika'))
# print(dict_1.get('three','Ishika'))
# print(dict_1.fromkeys('one',4))
# print(dict_1.fromkeys(('one','two'),3))
# print(dict_1.fromkeys(['one','two'],3))
# print(dict_1.fromkeys({'one','two'},3))
# print(dict_1.fromkeys({'one':1,'two':2},3))
dict_a = {'one':1,'two':2,}
print(dict_a)
print(dir(dict_a))
# help(dict_a.pop)

print(dict_a.pop('two'))
print(dict_a)
print(dict_a.pop('one'))
print(dict_a)
dict_a = {'one':1,'two':2}
print(dict_a)
# popitem follows last in first out
# help(dict_a.popitem)
print(dict_a.popitem())
print(dict_a.popitem())
print(dict_a)
help(dict_a.update)
dict_a.update([("a",1),("b",2)])
print(dict_a)
dict_a.update({"a":1,"b":2,"c":3,"d":4})
print(dict_a)




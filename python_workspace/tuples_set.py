# Tuples are immutable andare faster than list as they just have two function 
# while passing just one value in tuple we need to put , after that value 
tuples = (1,2,2,1,3,2,2,1,4,5,1,2,3,2,6,6,)
tu = ('hiee', 'hello')
print(tuples)
print(tuples.count(3))
print(tuples.count(2))
print(tuples.index(4))
print(tuples.index(6))
# set
# set is a collection of dstinct element, can be letter ,people,numbers ,lines,variables
# set_1 = (1,2,3)
# print(type(set_1)) tuple type
set_1 = {1,2,3}
print(set_1)
r = {3,4,5,6}
li = [1,2,2,3,3,4,5,6,7,8,2,2,4,4]
r = set(li)
print(r)
# print(dir(set_1))
# set_1[0] = 7
i = {1,2,3,4,5}
j = {2,3,4,5,6,7}
print(i)
print(j)
print(i.difference(j))
print(j.difference(i))
print(i.union(j))
print(set_1.union(r))

set_m = {0,1,2,3,4,5,6,7,8,9}
set_n = {1,2,3,4,5,6,7,9,11,12}
set_n.update({13,24,25})
print(set_m)
print(set_m.isdisjoint(set_n))
u = {1,2,3}
l = {4,5,6}
print(u.isdisjoint(l))
print(set_m.intersection(set_n))
print(set_m.issubset(set_n))
print(set_n.issubset(set_m))
set_m.discard(0)
set_m.discard(8)
print(set_m)
print(set_m.issubset(set_n))


#set
s = set()
l = [1,2,3,4,5]
s_of_set = set(l)
print(s_of_set)
print(type(s_of_set))
s.add(2)
s.add(5)
print(s)
print(type(s))
s1 = s.union({1,2,5})
s1 = s.intersection({1,2,6})
print(len(s))
print(max(s))
print(min(s))
s1 = s.difference({2})
print(s1)
s1 = {5.3}
#s.isdisjoint()
print(s.isdisjoint(s))
#Assume that the operation are executed in order. What will each print display:

a = 2
b = 3
c = "abc"
print(a, b, c) #2 3 abc
print(a, b, c, sep = " : ") #2 : 3 : abc
a += 2
a == 5
print(a) #4
print(c*(a-b)) #abc
d = c.find("b")
print(d) #1
print(d and b) #3
print(d == True) #True
e = str(a) + str(b) + str(c) + str(d)
print(e) #43abc1
print(e[1::2]) #3b1
print(e+e[::-1]) #43abc11cba34
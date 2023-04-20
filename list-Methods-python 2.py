



#-----------
#---Lists Methods-----
#-----------



# Clear()

x = [1,2,3,4]
x.clear()
print(x) # []


# Copy()

a = [1,2,3,4]
c = a.copy()

print(a) # Main List # [1, 2, 3, 4]
print(c) # Copied List # [1, 2, 3, 4]

a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(c) # [1, 2, 3, 4]


# Count()

r = [1,5,7,2,5,4,8,0,25,62,44,5]
print(r.count(5)) # 3


# Index()

e = ["salar" , "Shergo" , "Lava" , "faten" , "Raman" , "Shergo" ]
print(e.index("Shergo")) # 1


# Insert()


s = [1,2,3,4 ,"A","B"]
s.insert(0,"test") # ['test', 1, 2, 3, 4, 'A', 'B']
s.insert(-1,"test") # ['test', 1, 2, 3, 4, 'A', 'test', 'B']
print(s)

# pop()

g = [1,2,3,4,5,"a","D"]
print(g.pop(2)) # 3
print(g.pop(-1)) # D
print(g) # [1, 2, 4, 5, 'a']






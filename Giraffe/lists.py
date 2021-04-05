homies = ["raph","soph","grace","fano","kerwin"]
print(homies[3:])

print(homies[1:3])
homies[2] = "grace2"
print(homies[2])

#nums=[4,8,15,16,23,42]
#homies.extend(nums)
#print(homies)

homies.append("bob")
print(homies)

homies.insert(0,"test")
print(homies)

homies.remove("test")
print(homies)

#homies.clear()
#print(homies)

homies.pop()
print(homies)

print(homies.index("raph"))
#print(homies.index("re"))

print(homies.count("raph"))

homies.sort()
print(homies)

homies.reverse()
print(homies)

homies2 = homies.copy()
print(homies2)
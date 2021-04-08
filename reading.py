doggiesFile = open("dogs.txt","r")
#r=read mode
#w=write mode
#a=apend, add new info
#r+= reading and writing
print(doggiesFile.readable())

#print(doggiesFile.readline())
#print(doggiesFile.readline())

#print(doggiesFile.readlines())

print(doggiesFile.readlines()[1])
'''
for dog in doggiesFile.readlines():
    print(dog)
'''
doggiesFile.close()

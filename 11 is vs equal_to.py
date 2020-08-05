#is --> Checks object identity
#== --> Checks value equality of 2 objects

li1=[1,2]
li2=li1
li3=[1,2]

print("is:",li1 is li2,"\t==:",li1 == li2)  #Same object

print("is:",li1 is li3,"\t==:",li1 == li3)  #Diff objects with same value
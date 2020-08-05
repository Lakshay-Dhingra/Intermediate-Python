str="Python is Fun!"
#Creating a byte object corresponding to str
bytes_obj=bytes(str,'utf-8')
#It displays the ascii of each byte when printed
print(bytes_obj)

var=5
bytes_arr=bytes(5)
print(bytes_arr)

li=[1,2,3,4]
bytes_arr=bytes(li)
print(bytes_arr)

str="Python is Fun!"
#Creating a byte object corresponding to str
bytes_obj=bytearray(str,'utf-8')
#It displays the ascii of each byte when printed
print(bytes_obj)

var=5
bytes_arr=bytearray(5)
print(bytes_arr)

print("Putting a list in file via bytearray():")
li=[1,2,3,4]
bytes_arr=bytearray(li)
print(bytes_arr)

file_obj=open("lak4.txt","wb+")
file_obj.write(bytes_arr)
file_obj.seek(0)
data=file_obj.read()
print("Obtaining a list:")
print(list(data))
file_obj.close()
print()

print("Printing binary numbers:",0b11010101)
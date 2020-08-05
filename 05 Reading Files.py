# open lak.txt
import sys
try:
    file_name=sys.argv[1]
except:
    sys.exit("Please Provide the Filename!")

file_obj=open(file_name)
#The file object will be created and assigned to file_obj

print(f"\nReading the file {file_name}: ")
print(file_obj.read())

#I've to open the file again bcz its pointer has reached at EOF now.
file_obj=open(file_name)
print(f"\nReading the first 20 characters of {file_name}:")
print(file_obj.read(20))

file_obj=open(file_name)
print(f"\nReading the {file_name} line by line:")
for line in file_obj:
    print(line,end="")
print()

file_obj=open(file_name)
print(f"\nReading the {file_name} line by line using readlines():")
file_list=file_obj.readlines()
for line_no,line in enumerate(file_list):
    print(line_no,line,end="")
print()

file_obj=open(file_name)
print(f"\nReading the {file_name} line by line using readline():")
str=file_obj.readline()
while(str!=""):
    print(str,end="")
    str=file_obj.readline()
print()

file_obj.close()
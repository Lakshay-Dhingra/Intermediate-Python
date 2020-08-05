file_obj=open("lak3.txt")

# To check if file is opened or not .closed is used
if file_obj.closed:
    print("File is closed...")
else:
    #.mode gives the mode in which file is opened.
    #.name gives name of the file

    print(f"File {file_obj.name} is opened in {file_obj.mode} mode.")
    print("Now closing the file.")
    file_obj.close()
print()

print("Opening file using with:")
with open("lak3.txt","rb+") as file_obj:
    print(f"File {file_obj.name} is opened in {file_obj.mode} mode.")
if file_obj.closed:
    print("File is closed...")
print()

print("Writing and reading from file:")
file_obj=open("lak3.txt","r+")
para=["Hi! How are you?\n", "I'm doing good, feel the happiness.\n"]
file_obj.writelines(para)
file_obj.seek(0)
print("File:",file_obj.read())
print()

file_obj.seek(0)
print("Truncating file upto 10 characters: ")
file_obj.truncate(10)
print("File:",file_obj.read())
print(f"Now the file pointer is at {file_obj.tell()}th index.")
print()

print("Now lets remove first 5 chars from the file")
file_obj.seek(5)
print(f"Now the file pointer is at {file_obj.tell()}th index.")
file_obj.truncate(5)
file_obj.seek(0)
print("File:",file_obj.read())
print()

print("Lets write something in the file:")
file_obj.write(" This is additional text.")
file_obj.seek(0)
print("File:",file_obj.read())
print()

print("Lets eraase the whole file.")
file_obj.seek(0)
file_obj.truncate()
file_obj.seek(0)
print("File:",file_obj.read())
print()

file_obj.close()


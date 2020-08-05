string="hello world"
#By default any string is in unicode encoding
#But python supports utf-8 by default
#encode() converts unicode string to utf-8 string byte object
byte_string=string.encode()
print(byte_string)

file_obj=open("lak5.txt","wb")
file_obj.write(byte_string)
file_obj.close()

file_obj=open("lak5.txt","rb")
byte_string2=file_obj.read()
file_obj.close()

#encode() converts byte to utf-8 string
string2=byte_string2.decode()
print(string2)

string="pythön!"

print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

# By default, encode() method doesn't require any parameters.
# It returns utf-8 encoded version of the string. In case of failure, it raises a UnicodeDecodeError exception.
# However, it takes two parameters:

    # encoding - the encoding type a string has to be encoded to

    # errors - response when encoding fails. There are six types of error response
    
    #     strict - default response which raises a UnicodeDecodeError exception on failure
    #     ignore - ignores the unencodable unicode from the result
    #     replace - replaces the unencodable unicode to a question mark ?
    #     xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
    #     backslashreplace - inserts a \uNNNN escape sequence instead of unencodable unicode
    #     namereplace - inserts a \N{...} escape sequence instead of unencodable unicode

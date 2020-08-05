#Some integer methods:
x=4
print(x.bit_length()) #100 3bits reqd

x=16
print(x.to_bytes(length=1,byteorder="big"))

x=-16
print(x.to_bytes(length=1,byteorder="big",signed=True))

print(int.from_bytes(b'\x00\x10', byteorder='little'))
print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))

print()

#Some Float methods
y=6.125
print(y.as_integer_ratio())

y=3.2
print(y.is_integer())
print()

y=5.0
print(y.is_integer())

y=5.000000000001
print(y.is_integer())


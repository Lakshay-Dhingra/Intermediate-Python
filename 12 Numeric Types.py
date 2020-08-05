# int() and float() data type
x=10
y=int(3.5)

#binary string converted to decimal
#decimal for 100 is 4
z1=int('0b100', base=0)

#octal number string converted to decimal
# decimal for 64 is 52
z2=int("64", base=8)

print(x,y,z1,z2)

# Automatically conerts to float
print(55.5/x)
print(55/x)
print(10.2*5)

# divmod(x, y) returns the pair (x // y, x % y)
print(divmod(29,13))

a=int("10203")
b=float("23.45")
print(a,b)

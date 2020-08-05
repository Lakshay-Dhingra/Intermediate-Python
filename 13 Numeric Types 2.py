# complex()

x=complex(24,-3)
print(x)

# y=complex("13","7") --> Invalid
y=complex("13+7j")
print(y)

z=complex(16.5,2.3)
print(z)

print("Adding and subtracting complex numbers:",x+y,y+z-x)
print("Multiplying and dividing complex numbers:",x*y,y/z)
print("Taking power of complex numbers:",x**2)
print(f"conjugate of {x} is {x.conjugate()}")
print(f"Real and Imaginary part of {x} are {x.real} and {x.imag}")
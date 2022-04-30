# Exploring data types in Python

# string
x = "Hello World"
print(x, type(x))

# int
y = 20
print(y, type(y))

# float
z = 39.1
print(z, type(z))
f = 35e3 # scientific notation indicating power of 10
print(f, type(f))

# bool
b = True
print(b, type(b))

# complex
i = 1j
print(i, type(i))

# list
fruits_list = ["grapes", "apples", "bananas"]
print(fruits_list, type(fruits_list))

# tuple
fruits_tuple = ("grapes", "apples", "bananas")
print(fruits_tuple, type(fruits_tuple))

# range
some_range = range(9)
print(some_range, type(some_range))

# frozenset
frozen_fruits = frozenset({"grapes", "apples", "bananas"})
print(frozen_fruits, type(frozen_fruits))

# bytes
some_bytes = b"Beautiful"
print(some_bytes, type(some_bytes))

# bytearray
a_bytearr = bytearray(7)
print(a_bytearr, type(a_bytearr))

# memoryview
m_view = memoryview(bytes(5))
print(m_view, type(m_view))

# None
n = None
print(n, type(n))

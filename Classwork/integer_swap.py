"""
a = 5                 
b = 10               
c = a
d = b


print("a=", c, "b=", d)

 Assigning b to a """
""" A student wants to swap a = 5 and b = 10 so that a becomes 10 and be b = 5. they write a = b and b = a. Explain the bug, write the correct solution  """
a = 5
b = 10

a,b = b,a

print("a =",a,"b =", b)


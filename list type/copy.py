num1 = [10,20,30]

"""
num2 = num1

print(id(num1))
print(id(num2))
print(num2)
print(num1)

num1.append(40)

print(id(num1))
print(id(num2))
print(num1)
print(num2)

# if we want to copy an array, we can't do like above
"""
num3 = num1.copy()

num1.append(40)

print(id(num1),id(num3))
print(num1,num3)

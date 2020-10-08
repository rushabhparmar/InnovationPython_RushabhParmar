# Answer 1

x = 1; y = 2.5; z = "String"
print(x)
print(y)
print(z)

# Answer 2

x = 1 + 2j
print(type(x))

y = 2
print(type(y))

x = y
print(type(x))

# Answer 3

# Method 1
x = 1
y = 2
result = x
x = y
y = result

print(x)
print(y)

# Method 2
x,y = y,x

print(x)
print(y)

# Answer 4

#Python 2
# UserValue = raw_input(“Enter value:”)
# Print UserValue
#Python 3
# UserValue = input(“Enter value:”)
# Print(UserValue)

# Answer 5

x = int(input("Enter any number between 1-10:"))
y = int(input("Enter another number between 1-10:"))
z = x + y
result = z + 30
print("Your final answer is -", result)

# Answer 6

x = input("Enter anything:")
print("The input value data type is -", type(x))

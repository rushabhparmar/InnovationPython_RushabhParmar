# Answer 1

x = int(input("Enter any number:"))

if x%3 == 0 and x%5 != 0:
    print("ConsultAdd")

if x%5 == 0 and x%3 != 0:
    print("c")

if x%3 == 0 and x%5 == 0:
    print("ConsultAdd Python training")
    
else:
    print("Number is non-divisible by 3 or 5.")


# Answer 2

print("Enter the number for the operation to be performed:", 
"\r\n 1 - Addition", "\r\n 2 - Subtraction","\r\n 3 - Multiplication","\r\n 4 - Division\r\n 5 - Average")
x = int(input("Enter selection: "))
Number1 = int(input("Enter 1st number: "))
Number2 = int(input("Enter 2nd number: "))

if x == 1:
    Addition = Number1 + Number2
    print(Addition)
    if Addition < 0:
        print("Negative")
if x == 2:
    Subtraction = Number1 - Number2
    print(Subtraction)
    if Subtraction < 0:
        print("Negative")
if x == 3:
    Multiplication = Number1 * Number2
    print(Multiplication)
    if Multiplication < 0:
        print("Negative")
if x == 4:
    Division = Number1 / Number2
    print(float(Division))
    if Division < 0:
        print("Negative")
if x == 5:
    Number3 = int(input("Enter 3rd number: "))
    Number4 = int(input("Enter 4th number: "))
    Average = (Number1 + Number2 + Number3 + Number4)/4
    print(Average)
    if Average < 0:
        print("Negative")

# Answer 3

a = 10
b = 20 
c = 30
avg = (a+b+c)/3

if avg > a and avg > b and avg > c:
    print("Average is greater than a, b, and c")
elif avg > a and avg > b:
    print("Average is greater than a and b")
elif avg > a and avg > c:
    print("Average is greater than a and c")
elif avg > b and avg > c:
    print("Average is greater than b and c")
elif avg > a and avg < b and avg < c:
    print("Average is just greater than a")
elif avg < a and avg > b and avg < c:
    print("Average is just greater than b")
elif avg < a and avg < b and avg > c:
    print("Average is just greater than c")

# Answer 4

while True:
    UserInput = int(input("Enter positive number to continue and negative number to discontinue: "))
    if UserInput < 0:
        print("It's over!")
        break
    else:
        print("Going good..")
        continue

# Answer 5

for i in range(2000,3200):
    if i%7 == 0 and i%5 != 0:
        print(i)

# Answer 6

x=123 
for i in x:
    print(i)

# for i in x:
# TypeError: 'int' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")

# 0
# 1
# 2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# 0
# 1
# 2
# 3
# 4

# Answer 7

for i in range(6):
    if (i == 3 or i == 6):
        continue
    print(i)

# Answer 8

x = input("Enter a string: ")
d = l = 0
for i in x:
    if i.isdigit():
        d = d+1
    elif i.isalpha():
        l = l+1
    else:
        pass
print("# of Letters: ",l)
print("# of Digits: ",d)

# Answer 9

#Part1
while True:
    x = int(input("Guess the lucky number: "))
    y = 19
    if x == y:
        break
    else:
        continue
    

#Part2
while True:
    x = int(input("Guess the lucky number: "))
    y = 19
    if x == y:
        break
    else:
        ans = str(input("Want to guess again? (yes/no): "))
        if ans == 'no':
           break
        else:
            continue

# Answer 10 & 11

c = 1
n = 19
while c <= 5:
    g = int(input("Enter your guess: "))
    print("Trial number",c)
    c = c + 1
    if g == n:
        print("Good guess!")
        break
    else:
        print("Try again!")
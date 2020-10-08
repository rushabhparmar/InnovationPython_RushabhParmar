#Answer 1

new_list = ['5', "five", "1+2j","2.5"]
print(type(new_list))

#Answer 2

numbers = [10, 20, 30, 40, 50]
nums = numbers[2:4]
print(nums)

#Answer 3

def sum_mul():
    numbers = [1,2,3,2]
    total = 0
    for i in range(0, len(numbers)):
        total = total + numbers[i] 
    print("sum of all numbers in a list:", total)

    result = 1
    for x in numbers: 
        result = result * x  
    print("Multiplication of all numbers in a list:",result)

sum_mul()

#Answer 4

l = [10,200,2000,0.5]
min_no = min(l)
print(min_no)

max_no = max(l)
print(max_no)

#Answer 5

mix_list = [1,2,3,4,5,6,7,8,9,10]

new_list = []
for i in (mix_list):
    if i%2 == 0:
        new_list.append(i)
print(new_list)

#Answer 6

new_list = []
for i in range(1,30):
    new_list.append(i**2)
print(new_list)
print("first five elements", new_list[:5])
print("last five elements", new_list[-5:])

#Answer 7

sample_data1 = [1,3,5,7,9,10]
sample_data2 = [2,4,6,8]

sample_data1[-1:] = sample_data2
print(sample_data1)

#Answer 8

a={1:10,2:20}
b={3:30,4:40}

c = {}
for d in (a, b):
    c.update(d)

print(c)

#Answer 9

def dictionary(size):
    d = {}

    for item in range(1, size+1):
       d[item]=item*item

    print(d)

dictionary(5)

#Answer 10 

values = input("Input some comma seprated numbers : ").split(",")
list = values
tuple = tuple(list)
print('List values : ',list)
print('Tuple values : ',tuple)

#Answer 11

list1 = ["1", "2", "a", "b", "2.3", "5.6", "random", "name", "3+1i", "5"]

#Answer 12

numbers = [10, 20, 30, 40, 50]
nums = numbers[:4]
print(nums)

#Answer 13

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

# ●	Access list [1, 2, 3, 4]
print(x[5][:4])
# ●	Access list [600,  700]
print(x[-3:-1])
# ●	Access list [100, 300, 500, 600, 800]
print(x[::2])
# ●	Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
x.reverse()
print(x)
# ●	Access list [10]
print(x[5][5][:1])
# ●	Access list [ ]
del x[:]
print(x)

#Answer 14

x = range(1,1000)
y = xrange(1,1000)

print(type(x))
print(type(y))

#Answer 16

a = range(1,100)
l = []
for i in a:
    if i%3 == 0 and i%2 ==0:
        l.append(i)
print(l)

#Answer 17

vowels = "a","e","i","o","u"
string = input("Enter a string: ")
rev_string = string[len(string)::-1]

print("Reverse string: ",rev_string)

for string in rev_string:
    if string in vowels:
        print("Vowels in string:",string)

#Answer 18

def printEvenWords(x): 
    x = x.split(' ')   
    for word in x:    
        if len(word)%2 == 0: 
            print(word)  
 
x = input("Enter a sentence: ") 
printEvenWords(x) 

#Answer 19

x = [1,2,3,4,5,6,7,8,9,-1]
y = []
for i in x:
    for j in x:
        if i+j == 8:
            print(i,j)

# #Answer 20

# Task 20.1

even_list = [] #Task 1
odd_list = []

while True:
    number=int(input("enter the no in range of 1-50: ")) #Task 2
    if number%2 == 0:
        even_list.append(number)
        if len(even_list) == 5: #Task 3
            break
    else:
        odd_list.append(number)
        if len(odd_list) == 5:
            break

    
print("Even list: ", even_list)
print("Sum of Even list is: ", sum(even_list)) #Task 4

print("Max of Even list is: ", max(even_list))

print("Odd list: ", odd_list)
print("Sum of Odd list is: ", sum(odd_list))
print("Max of Odd list is: ", max(odd_list))

#Answer 21

x = "2abcbacbaba344ab"
y = {}
for i in x:
    if i.isalpha():
        if i in y:
            y[i]+=1
        else:
            y[i]=1
    else:
        pass

print(y)

#Answer 22

x = (1,2,3,4,5,6,7,8,9,10)
y = []
for i in x:
    if i%2 == 0:
        y.append(i)

z = tuple(y)
print(z)
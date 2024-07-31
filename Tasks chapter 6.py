################################################################## Practice

#task 1
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
def MaxNum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(MaxNum(a, b, c))


#task2
text = input("Enter a text: ")
vowel = ('AaEeOoIiUuYy')
def lettcou(a):
    count = 0
    for letter in a:
        for i in vowel:
            if letter == i:
                count += 1
    print(count)
lettcou(text)


#task3
a = int(input("Enter a len: "))
def numcou(a):
    count = 0
    for i in range(a):
        if int(input("Enter a number: ")) != 0:
            count += 1
    return count
print(numcou(a))


#task4
a = input("Enter a password: ")
def checkpass(x):
    count1 = 0
    count2 = 0
    count3 = 0
    for letter in x:
        if letter.isupper() == True:
            count1 += 1
        elif letter.islower() ==  True:
            count2 += 1
        elif letter.isdigit() == True:
            count3 += 1
    if count1 >= 3 and count2 >= 3 and count3 >= 1:
        print("Password is correct")
    else:
        print("Try again")
checkpass(a)


#task5
size = int(input("Enter a length: "))
arr = []
for i in range(size):
    arr.append(int(input("Enter a number: ")))
def task(arg):
    count = 0
    for i in arg:
        if i % 5 == 0 and i < 20:
            print(i)
        else:
            count = count + i
    print("Sum: ", count)
task(arr)


################################################################## Lab 1

#task1
size = int(input("Enter a length: "))
vowel = ('AaEeOoIiUuYy')
arr = []
for i in range(size):
    arr.append(input("Enter a text: "))
def checktext(array):
    arr1 = []
    for word in array:
        count = 0
        for letter in word:
            for i in vowel:
                if letter == i:
                    count += 1
        if count > 4:
            arr1.append(word)
    for x in arr1:
        print(x)
checktext(arr)


#task2
size = int(input("Enter a length: "))
arr = []
for i in range(size):
    arr.append(int(input("Enter a number: ")))
n = int(input("Enter a special number: "))
def task(arg, number):
    for i in range(len(arg)):
        if i == arg[i] and i % number != 0:
            print (arg[i])
task(arr, n)


#task3
text = input("Enter a text: ")
subtext = input("Enter a subtext: ")
def checktext(a, b):
    if b in a:
        print("Yes")
    else:
        print("No")
checktext(text, subtext)


#task4
N = int(input("Enter a length: "))
arr = []
for i in range(N):
    arr.append(int(input("Enter a number: ")))
def task(array):
    unique = []
    for i in range(N):
        count = 0
        for j in range(N):
            if array[i] == array[j]:
                count += 1
        if count == 1:
            unique.append(array[i])
    return unique
for i in task(arr):
    print(i, end=" ")


#task5
a = int(input("Enter i: "))
b = int(input("Enter j: "))
arr = []
for i in range(a):
    S = []
    for j in range(b):
        S.append(int(input("Enter the number: ")))
    arr.append(S)
def task(arg):
    count = 0
    for i in range(a):
        for j in range(b):
            if i % 2 != 0 and j % 2 != 0:
                count = count + arr[i][j]
    print("Sum: ", count)
task(arr)


################################################################## Practice 1

#task 1
n = int(input("Enter a length: "))
a = []
for i in range(n):
    num = int(input("Enter a number: "))
    a.append(num)
for i in range(n):
    print(a[i -1], end=" ")


#task 2
n = int(input("Enter a length: "))
a = []
for i in range(n):
    num = int(input("Enter a number: "))
    a.append(num)
summ = sum(a)
average = summ / n
print(summ, average)


#task 5
n = int(input("Enter a length: "))
a = []
for i in range(n):
    num = int(input("Enter a number: "))
    a.append(num)
print(a)
m = int(input("Enter m: "))
if m in a:
    i = a.index(m)
    print("Yes", "\nIndex: ", i)
else:
    print("No")


################################################################## Practice 2

#task 1
a = "Hi ! I am number 1. I was born in 1990. I read 5 books and eat 2 apples."
b = list()
for i in a:
    if i.isdigit():
        b.append(i)
print(b)


#task 2
a = str(input("Enter a text: "))
b = a.split(' ')
print(b)
n = int(input("Enter a number: "))
c = b[n-1]
print(c[0])


#task 3
a = str(input("Enter a text: "))
b = a.split(' ')
c = []
for i in range(len(b)):
    c.append(b[len(b)-i-1])
print(c)


#task 5
a = str(input("Enter a text: "))
b = a.split(' ')
print(sorted(b, key=len))


################################################################## Lab 1
#task6
n = int(input("Enter a length: "))
a = []
c = []
for i in range(n):
    num = int(input("Enter a number: "))
    a.append(num)
print("The list of entered numbers: ", a)
for x in range(n):
    if a[x] == 0:
        c.append(x)
print("The indexes of '0': ", c)
a = a[c[0]+1:c[1]]
print("The sum of numbers between two '0': ", sum(a))


################################################################## Lab 2
#task3
a = str(input("Enter an a text: "))
b = str(input("Enter a b text"))
if b in a:
    print("Yes")

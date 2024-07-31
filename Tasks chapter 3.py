
################################################################## Practice
#task 1
n = int(input("Enter a number: "))
i=1
for i in range(1,n+1):
    print(i, pow(i, 2))


#task 2
n = int(input("Enter a number: "))
formula = sum(i**3 for i in range(1, n+1))
print("The sum = "+str(formula))


#task 3
numbers = []
n = -99999999999
while n != 0:
    n = int(input("Enter a number: "))
    numbers.append(n)
    if n == 0:
        break
print("\nMax number is: " + str(max(numbers)))


#task 4
a = int(input("Insert a: "))
b = int(input("Insert b: "))
for n in range(b+1):
    res = a**n
    print(str(a)+"^"+str(n)+" = "+str(res))


#task 5 !!!
odd = []
n = 1
while n != 0:
    n = int(input("Enter a number: "))
    if n % 2 != 0:
        odd.append(n)
    elif n % 2 == 0:
        continue
    elif n == 0:
        break
print(sum(odd))


################################################################## LAB-1

#task1
n = int(input("Enter a number: "))
a = 1
for i in range(1, n+1):
    a = a*i
print(a)


#task2
nums = []
a = 1
while a != 0:
    n = float(input("Enter a number: "))
    if n != 0:
        nums.append(n)
    elif n == 0:
        break
print(nums)
for i in nums:
   a = a*i
res = round(a, 2)
print("The result: "+str(res))


#task3
n = int(input("Enter a number: "))
a = 0
for i in range(1, n+1):
    a = a + 1/i
print(a)


#task4 ??? problems
a = int(input("Please insert a: "))
b = int(input("Please insert b: "))
result = 1

for i in range(b):
    result *= a

print(result)


################################################################## LAB-2

#task1
x = int(input("Insert x: "))
for i in range(1,x+1):
    if x % i == 0:
        print(i, end=" ")


#task2
a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))
d = int(input("Insert d: "))
for i in range(a,b):
    if i % d == c:
        print(i, end=" ")


#task3
nums = []
count = 0
a = 1
while a != 0:
    n = int(input("Enter a number: "))
    if n != 0:
        nums.append(n)
        count = count + 1
    elif n == 0:
        break
res = sum(nums)/count
print(count, "numbers entered")
print("The average value is: ", round(res, 2))


#task4
n = int(input("Enter a number: "))
res = 2**n
print("The result: ", res)


#task5
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i**2
print(sum)


#task6
n = input("Enter a number: ")
a = []
for i in n:
    a.append(int(i))
print(sum(a))


#task7
a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))
d = int(input("Insert d: "))
for x in range(0, 1000):
    if a * (x**3) + b * (x**2) + c * x + d == 0:
        print("The result is: ", x)


################################################################## LAB-3

#task1
n = int(input("Enter a number: "))
a = 1
for i in range(1, n+1):
    a = a * (1 + 1 / i**2)
print(a)


#task2

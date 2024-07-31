################################################################## Practice

#task 1
N = int(input('Enter quantity of i: '))
M = int(input('Enter quantity of j: '))
a = []
for i in range(N):
    S = []
    for j in range(M):
        S.append(int(input('Enter number: ')))
    a.append(S)
a[0], a[-1] = a[-1], a[0]
for row in a:
    print(' '.join([str(elem) for elem in row]))


#task 2
n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
a = []
for i in range(n):
    S = []
    for j in range(m):
        if (i + j) % 2:
            S.append(0)
        else:
            S.append(1)
    a.append(S)
for row in a:
    print(' '.join([str(elem) for elem in row]))


#task 3
n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
a = []
for i in range(1, n+1):
    S = []
    for j in range(1, m+1):
        S.append(i*j)
    a.append(S)
for row in a:
    print(' '.join([str(elem) for elem in row]))


#task 4
n = int(input("Enter a range: "))
a = {k: k**2 for k in range(1, n+1)}
print(a)


#task 5
employee = {
'employee1': {'name': 'Sam', 'age': 35, 'salary': 400000},
'employee2': {'name': 'Anna', 'age': 29, 'salary': 350000},
'employee3': {'name': 'John', 'age': 25, 'salary': 250000}
}
employee['employee3']['salary'] = 300000
print(employee)


#task 6
size = int(input("Enter a size: "))
synonyms = {}
for i in range(size):
    word = input("Enter a word: ")
    synonyms[word] = input("Enter a synonym: ")
a = input("Enter a word from synonyms: ")
print(synonyms[a])


################################################################## Lab 1
#task 1
M = int(input('Enter quantity of i: '))
a = []
for i in range(2):
    S = []
    for j in range(M):
        S.append(int(input('Enter number: ')))
    a.append(S)
if a[1] == a[0]:
    print("Yes")
else:
    print("No")


#task 2
N = int(input('Enter quantity of i: '))
M = int(input('Enter quantity of j: '))
a = []
count = 0
for i in range(N):
    S = []
    for j in range(M):
        S.append(int(input('Enter number: ')))
    a.append(S)
for i in range(N):
    for j in range(M):
        if a[i][j] < 0:
            count += 1
            a[i][j] = 'x'
        print(a[i][j], end=' ')
    print()
print('Number of x: ', count)


#task 3
N = int(input('Enter quantity of i: '))
M = int(input('Enter quantity of j: '))
a = []
for i in range(N):
    S = []
    for j in range(M):
        S.append(int(input('Enter number: ')))
    a.append(S)
for i in range(N):
    count = 0
    for j in range(M):
        if a[i][j] < 0:
            count += 1
    print('Number of x on ' + str(i+1) + '-row: ', count)


#task 4
N = int(input('Enter quantity of i and j: '))
a = []
for i in range(N):
    S = []
    for j in range(N):
        S.append(int(input('Enter number: ')))
    a.append(S)
for i in range(N):
    for j in range(N):
        if i == j:
            a[i][j] = 'x'
        print(a[i][j], end=' ')
    print()


#task5
N = int(input('Enter quantity of i and j: '))
a = []
count = 0
for i in range(N):
    S = []
    for j in range(N):
        S.append(int(input('Enter number: ')))
    a.append(S)
for i in range(N):
    for j in range(N):
        if a[i][j] == a[j][i]:
            count += 1
if count == N*N:
    print('\nYes')
else:
    print('\nNo')


#task6
users = {
    "user": "qwerty", "user2": "qwerty2", "user3": "qwerty3"
}
a = input("Insert login: ")
b = input("Insert password: ")
if users[a] == b:
    print("\nAuthentication completed")
else:
    print("\nIncorrect login or password")

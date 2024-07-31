################################################################## Practice 1

#task 1
import os
arr = []
err = []
result = []
f = open("input.txt", "r")
for i in f.read():
    try:
        res = int(i)
        arr.append(res)
    except ValueError:
        err.append('Invalid value')
result.append(min(arr))
result.append(max(arr))
f.close()

f1 = open("file1.txt", "w")
for i in result:
    f1.write(str(i) + ' ')
f1.close()


#task2
import os
arr = []
err = []
result = []
f = open("input.txt", "r")
for i in f.read():
    try:
        res = int(i)
        arr.append(res)
    except ValueError:
        err.append('Invalid value')
result = sorted(arr)
f.close()

f1 = open("file2.txt", "w")
for i in result:
    f1.write(str(i) + ' ')
f1.close()


#task3
import os
linecount = 0
f = open("file3.txt", "r")

for line in f:
    print(str(len(line)), "symbols.")
    print(str(line))
    linecount += 1
print("\n", linecount, "lines.")
f.close()


################################################################## Lab 1

#task1
class User:
    id = 0
    login = ''
    password = ''

    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password

    def toString(self):
        return f"\nID: {self.id}, login: {self.login}, password: {self.password}"


def getUsersList():
    file = open("memory.txt", "r")
    print(file.read())
    file.close()


def saveUser(user):
    file = open("memory.txt", "a")
    file.write(user.toString())
    file.close()

while True:
    print("\nPRESS [1] TO ADD USERS\nPRESS [2] TO LIST USERS\nPRESS [4] TO EXIT")
    number = int(input("Enter your choice: "))
    if number == 1:
        ID = input("Enter ID: ")
        login = input("Enter login: ")
        password = input("Enter password: ")
        user1 = User(ID, login, password)
        saveUser(user1)
        print("USER ADDED\n")
    elif number == 2:
        print("LIST OF USERS:")
        getUsersList()
    elif number == 4:
        print("EXITED")
        break

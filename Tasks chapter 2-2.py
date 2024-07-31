################################################################## Practice 1

#task 1
a = input("Insert a: ")
b = input("Insert b: ")
try:
    res = int(a)
    res1 = int(b)
    print(res + res1)
except:
    print(str(a) + str(b))


#task 2
class Class:
    name = ''
    surname = ''
    age = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

users = []
sum = 0

for i in range(5):
    name = input('Enter a name: ')
    surname = input('Enter a surname: ')
    age = input('Enter an age: ')
    try:
        res = int(age)
        users.append(Class(name, surname, age))
    except:
        users.append(Class(name, surname, 0))

for user in users:
    print(user.name, user.surname, user.age)
    sum = sum + int(user.age)

average = sum / len(users)
print(average)

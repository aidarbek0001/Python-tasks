################################################################## Practice

#task 1
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def printData(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} USD")


class Programmer(Employee):
    def __init__(self, name, age, salary, programmingLanguage):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary
        self.programmingLanguage = programmingLanguage

    def printData(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} USD, Programming Language: {self.programmingLanguage}")


class DataPartner(Employee):
    def __init__(self, name, age, salary, databaseTool):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary
        self.databaseTool = databaseTool

    def printData(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} USD, Database Tool: {self.databaseTool}")

Dev1 = Programmer("Max", 30, 5000, "Java")
Dev2 = Programmer("Justin", 27, 4500, "Python")
Dev3 = Programmer("Kudaibergen", 25, 7000, "C++")

dat1 = DataPartner("Sam", 28, 4900, "Mongo")
dat2 = DataPartner("Emmy", 31, 5200, "MySQL")
dat3 = DataPartner("Beksultan", 26, 6400, "PostgresSQL")

Employees = [Dev1, Dev2, Dev3, dat1, dat2, dat3]
Summ = 0
NumberOfEmployees = len(Employees)
for emp in Employees:
    emp.printData()
for emp2 in Employees:
    Summ += emp2.salary
AverageSalary = int(Summ / NumberOfEmployees)
print(f"Average Salary: {AverageSalary}")


#task2
class User:
    id = 0
    login = ""
    password = ""
    name = ""
    surname = ""

    def __init__(self, id, login, password, name, surname):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname

    def getData(self):
        return self.id, self.login, self.password, self.name, self.surname


class Staff(User):
    salary = 0.0
    subjects = []

    def __init__(self, id, login, password, name, surname, salary, subjects):
        super().__init__(id, login, password, name, surname)
        self.salary = salary
        self.subjects = subjects

    def getData(self):
        return self.id, self.login, self.password, self.name, self.surname, self.salary, self.subjects

    def addSubject(self, subject):
        self.subjects.append(subject)


class Student(User):
    gpa = 0.0
    courses = []

    def __init__(self, id, login, password, name, surname, gpa, courses):
        super().__init__(id, login, password, name, surname)
        self.gpa = gpa
        self.courses = courses

    def getData(self):
        return self.id, self.login, self.password, self.name, self.surname, self.gpa, self.courses

    def addCourse(self, course):
        self.courses.append(course)

user1 = User(1, "John1", "qwer1", "John", "Smiths")
user2 = User(2, "John2", "qwer2", "Johny", "Smooths")
user3 = User(3, "John3", "qwer3", "Johnathan", "Smiles")
user4 = User(4, "John4", "qwer4", "Johnie", "Smitt")
user5 = User(5, "John5", "qwer5", "John JR", "Smut")

staff1 = Staff(user1.id, user1.login, user1.password, user1.name, user1.surname, 250000, [])
staff2 = Staff(user2.id, user2.login, user2.password, user2.name, user2.surname, 220000, [])
staff3 = Staff(user3.id, user3.login, user3.password, user3.name, user3.surname, 230000, [])
staff4 = Staff(user4.id, user4.login, user4.password, user4.name, user4.surname, 240000, [])
staff5 = Staff(user5.id, user5.login, user5.password, user5.name, user5.surname, 260000, [])

student1 = Student(user1.id, user1.login, user1.password, user1.name, user1.surname, 3.1, [])
student2 = Student(user2.id, user2.login, user2.password, user2.name, user2.surname, 3.2, [])
student3 = Student(user3.id, user3.login, user3.password, user3.name, user3.surname, 3.3, [])
student4 = Student(user4.id, user4.login, user4.password, user4.name, user4.surname, 3.4, [])
student5 = Student(user5.id, user5.login, user5.password, user5.name, user5.surname, 3.5, [])

staff1.addSubject("Mathematics")
staff1.addSubject("Physics")

student1.addCourse("Calculus")
student1.addCourse("English Literature")


users = [user1, user2, user3, user4, user5, staff1, staff2, staff3, staff4, staff5, student1, student2, student3, student4, student5]
for user in users:
    print(user.getData())


################################################################## Lab 1

#task1
class Book:
    name = ""
    code = ""
    pages = 0
    def __init__(self, name, code, pages):
        self.name = name
        self.code = code
        self.pages = pages

    def getBookData(self):
        print("Name: ", self.name, "Code: ", self.code, "Pages:", self.pages)

class ScientificBook(Book):
    price = 0
    publisher = ""
    def __init__(self, name, code, pages, price, publisher):
        super().__init__(name, code, pages)
        self.price = price
        self.publisher = publisher

    def getBookData(self):
        print("Name: ", self.name, "Code: ", self.code, "Pages:", self.pages, "Price: ", self.price, "Publisher: ", self.publisher)

class LiteratureBook(Book):
    author = ""
    publishedYear = 0
    def __init__(self, name, code, pages, author, publishedYear):
        super().__init__(name, code, pages)
        self.author = author
        self.publishedYear = publishedYear

    def getBookData(self):
        print("Name: ", self.name, "Code: ", self.code, "Pages:", self.pages, "Author: ", self.author, "Published Year: ", self.publishedYear)

class Library:
    name = ""
    city = ""
    country = ""
    listBooks = []
    def __init__(self, name, city, country, listBooks):
        self.name = name
        self.city = city
        self.country = country
        self.listBooks = listBooks

    def addBook(self, book):
        self.listBooks.append(book)

    def printLibrary(self):
        print("Name: " + self.name + ", City: " + self.city + ", Country: " + self.country + ", ListBooks: ")
        for book in self.listBooks:
            book.getBookData()

lib1 = Library("Central Library", "London", "England", [])

book1 = ScientificBook("Astronomy", "A5F47", 210, 10000, "British Astronomy College")
book2 = ScientificBook("Geography", "A6S39", 300, 12000, "London Geo University")
book3 = LiteratureBook("Great Gatsby", "F9Q31", 180, "Francis Scott Key Fitzgerald", 1925)
book4 = LiteratureBook("How to Fall in Love", "L4A56", 256, "Cecelia Ahern", 2013)
book5 = LiteratureBook("Code da Vinci", "J5F18", 529, "Dan Brown", 2003)

lib1.addBook(book1)
lib1.addBook(book2)
lib1.addBook(book3)
lib1.addBook(book4)
lib1.addBook(book5)

lib1.printLibrary()

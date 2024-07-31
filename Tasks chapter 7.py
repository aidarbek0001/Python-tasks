################################################################## Practice

#task 1
class Student:
    id = 0
    name = ""
    surname = ""
    gpa = 0.0
    def __init__(self,id, name, surname, gpa):
        self.id = id
        self.name = name
        self.surname = surname
        self.gpa = gpa
    def getStudentData(self):
        print("Student ID: {0}, Name: {1}, Surname: {2}, GPA: {3}".format(self.id, self.name, self.surname, self.gpa))
student1 = Student(1, "Aidar", "Molzhigit", 3.10)
student2 = Student(2, "Indira", "Kapsalyamova", 3.53)
student3 = Student(3, "Aidos", "Maylau", 3.22)
student4 = Student(4, "Alibi", "Sapanov", 3.71)
student5 = Student(5, "Marlen", "Poluanov", 3.39)
StudentsList = [student1, student2, student3, student4, student5]
for student in StudentsList:
    student.getStudentData()


#task2
class Student:
    id = 0
    name = ""
    surname = ""
    gpa = 0.0
    def __init__(self,id , name, surname, gpa):
        self.id = id
        self.name = name
        self.surname = surname
        self.gpa = gpa
    def gpaInfo(self):
        return self.gpa
    def studentInfo(self):
        return self.name
def topStudent(students):
    max_gpa = 0
    for i in range(len(students)):
        if students[i].gpaInfo() > max_gpa:
            max_gpa = students[i].gpaInfo()
    for i in range(len(students)):
        if students[i].gpaInfo() == max_gpa:
            print("The top student is: ", students[i].studentInfo(), "with gpa: ", max_gpa)

student1 = Student(1, "Aidar", "Molzhigit", 3.10)
student2 = Student(2, "Indira", "Kapsalyamova", 3.53)
student3 = Student(3, "Aidos", "Maylau", 3.22)
student4 = Student(4, "Alibi", "Sapanov", 3.71)
student5 = Student(5, "Marlen", "Poluanov", 3.39)
student6 = Student(6, "Karina", "Turbekova", 3.33)
student7 = Student(7, "Altay", "Aikeev", 3.42)
student8 = Student(8, "Aidos", "Asan", 3.28)
student9 = Student(9, "Ibragim", "Zholshibek", 3.65)
student10 = Student(10, "Zhuldyz", "Bekbolatkyzy", 3.56)

StudentsList = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]
topStudent(StudentsList)


#task3
class Student:
    name = ""
    surname = ""
    gpa = 0.0
    def __init__(self, name, surname, gpa):
        self.name = name
        self.surname = surname
        self.gpa = gpa
    def studentInfo(self):
        return ("{0} {1} {2}".format( self.name, self.surname, self.gpa))

StudentsList = []
number = 3
while number != 0:
    number = int(input("\nPRESS [1] TO ADD STUDENT \nPRESS [2] TO LIST STUDENT \nPRESS [0] TO EXIT\n"))
    if number == 1:
        student = Student(input("Insert name: "), input("Insert surname: "), float(input("Insert GPA: ")))
        StudentsList.append(student)
    elif number == 2:
        for id, student in enumerate(StudentsList, start=1):
            print(f"{id}) {student.studentInfo()}")
    elif number == 0:
        print("EXITED")
        break
    else:
        print("ENTER A VALID NUMBER!")
        number = int(input("\nPRESS [1] TO ADD STUDENT \nPRESS [2] TO LIST STUDENT \nPRESS [0] TO EXIT\n"))


################################################################## Lab 1

#task1
class Car:
    name = ""
    model = ""
    speed = 0
    weight = 0
    def __init__(self, name, model, speed, weight):
        self.name = name
        self.model = model
        self.speed = speed
        self.weight = weight
    def getData(self):
        print(f"Name: {self.name}, Model: {self.model}, Speed: {self.speed}, Weight: {self.weight}")
    def ride(self):
        print(f"\n{self.name} {self.model} is coming now with {self.speed} km/h.")

car1 = Car("BMW", "M5 F90", 250, 2000)
car2 = Car("Mercedes-Benz", "CLS 63 AMG", 250, 1700)
car3 = Car("Porsche", "Cayenne", 245, 1800)
car4 = Car("Toyota", "Camry 80", 230, 1600)
car5 = Car("Audi", "RS 7", 300, 1900)

CarList = [car1, car2, car3, car4, car5]
for car in CarList:
    car.getData()
car3.ride()


#task2
class Engine:
    def __init__(self, name, cylinderAmount, cylinderVolume, weight):
        self.name = name
        self.cylinderAmount = cylinderAmount
        self.cylinderVolume = cylinderVolume
        self.weight = weight
    def __str__(self):
        return f"{self.name}, {self.cylinderAmount} cylinders,{self.cylinderVolume}L, {self.weight}kg"
class Car:
    def __init__(self, name, model, speed, weight, engine):
        self.name = name
        self.model = model
        self.speed = speed
        self.weight = weight
        self.engine = engine
    def getData(self):
        print(f"Name: {self.name}, Model: {self.model}, Speed: {self.speed}km/h, Weight: {self.weight}kg, Engine: {self.engine}")
    def ride(self):
        print(f"\n{self.name} {self.model} is coming now with {self.speed}.")

def totalWeight(cars):
    totalCarWeight = 0
    totalEngineWeight = 0
    for car in cars:
        totalCarWeight += car.weight
        totalEngineWeight += car.engine.weight
    totalWeight = totalCarWeight + totalEngineWeight
    print(f"Total weight: {totalWeight}kg")

engine1 = Engine("2AR-FE", 4, 4, 147)
engine2 = Engine("G4KE", 4, 3.5, 136)
engine3 = Engine("Z18XER", 4, 3.2, 120)

car1 = Car("BMW", "M5 F90", 250, 2000, engine2)
car2 = Car("Mercedes-Benz", "CLS 63 AMG", 250, 1700, engine2)
car3 = Car("Porsche", "Cayenne", 245, 1800, engine2)
car4 = Car("Toyota", "Camry 80", 230, 1600, engine1)
car5 = Car("Audi", "RS 7", 300, 1900, engine3)
car6 = Car("Nissan", "GT-R", 320, 1700, engine1)

CarList = [car1, car2, car3, car4, car5, car6]
for car in CarList:
    car.getData()
car6.ride()
totalWeight(CarList)


#task3
class CPU:
    def __init__(self, cacheMemory, price, weight):
        self.cacheMemory = cacheMemory
        self.price = price
        self.weight = weight
    def __str__(self):
        return f"CPU: {self.cacheMemory}MB, {self.price}tg, {self.weight}kg"
class HDD:
    def __init__(self, memory, price, weight):
        self.memory = memory
        self.price = price
        self.weight = weight
    def __str__(self):
        return f"HDD: {self}GB, {self.price}tg, {self.weight}kg"
class Laptop:
    def __init__(self, name, price, weight, hardDiskDrive, cpuMemory):
        self.name = name
        self.price = price
        self.weight = weight
        self.hardDiskDrive = hardDiskDrive
        self.cpuMemory = cpuMemory

def getTotalPrice(laptops):
    HDDprice = 0
    laptopPrice = 0
    cpuPrice = 0
    for laptop in laptops:
        HDDprice += laptop.hardDiskDrive.price
        laptopPrice += laptop.price
        for cpu in laptop.cpuMemory:
            cpuPrice += cpu.price
    totalPrice = HDDprice + cpuPrice + laptopPrice
    print("Total price is: ", totalPrice, "tg")

def getTotalCPUMemory(laptops):
    cpuMemory = 0
    for laptop in laptops:
        for cpu in laptop.cpuMemory:
            cpuMemory += cpu.cacheMemory
    print("Total CPU cache memory: ", cpuMemory, "MB")

def getTotalWeight(laptops):
    HDDweight = 0
    laptopWeight = 0
    cpuWeight = 0
    for laptop in laptops:
        HDDweight += laptop.hardDiskDrive.weight
        laptopWeight += laptop.weight
        for cpu in laptop.cpuMemory:
            cpuWeight += cpu.weight
    totalWeight = HDDweight + cpuWeight + laptopWeight
    print("Total price is: ", totalWeight, "kg")

CPU1 = CPU(3000, 154000, 0.4)
CPU2 = CPU(2500, 136000, 0.3)
CPU3 = CPU(2200, 122000, 0.6)
CPUs1 = [CPU1, CPU1, CPU1, CPU1, CPU1, CPU1, CPU1, CPU1]
CPUs2 = [CPU2, CPU2, CPU2, CPU2]
CPUs3 = [CPU3, CPU3]

HDD1 = HDD(2000, 113500, 1.1)
HDD2 = HDD(1000, 95700, 1.4)
HDD3 = HDD(500, 64900, 1.6)

Laptop1 = Laptop("HP", 728000, 3.9, HDD1, CPUs1)
Laptop2 = Laptop("Lenovo", 684000, 4.3, HDD1, CPUs1)
Laptop3 = Laptop("Acer", 661000, 3.4, HDD2, CPUs2)
Laptop4 = Laptop("Asus", 713000, 2.8, HDD2, CPUs2)
Laptop5 = Laptop("Dell", 672000, 3.2, HDD2, CPUs3)
Laptop6 = Laptop("Fujitsu", 608500, 3.7, HDD2, CPUs3)

Laptops = [Laptop1, Laptop2, Laptop3, Laptop4, Laptop5, Laptop6]

getTotalPrice(Laptops)
getTotalCPUMemory(Laptops)
getTotalWeight(Laptops)

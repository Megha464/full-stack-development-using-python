# student = ("ram","sam","rana")
# print(student)
# print(student[2])


# ####tuple is a collection used to store multiple values####
# numbers = (10,20,30,40)
# print(numbers[2])
# print(numbers[0:2])

# data = (1,2,3)
# data[0] = 100
# print(data)


####multipale values###
# x=(1,2,3,2,1,1,1)
# print(x.count(1))
# print(x.count(2))
# x = ("apple", "banana", "graps", "banana")
# print(x.count("banana"))
# print(x.index("banana"))


# ##### slicing #####
# print(x[1:3])
# print(x[1:4])


# x ={1,2,3,2,1,1,1}
# print(x)
# data = {1,2,3}
# data.add(4)
# print(data)
# data.remove(2)
# print(data)

# a = {1,2,3}
# b = {3,4,5}
# print(a|b)

# a = {1,2,3}
# b = {3,4,5}
# print(a&b)

# def add(a, b):
#     print(a + b)
# add(10, 20)
# def sub(a, b):
#     print(a - b)
# sub(20, 10)
# def mul(a, b):
#     print(a * b)
# mul(10, 20)
# def div(a, b):
#     print(a / b)
# div(20, 10)

# def add(a,b):
#     print(a+b)
# add(10,20)


# def add(*numbers):

#     print(numbers)
# add(10, 20, 30, 40, 50,60)

# def add(*num):
#     total = 0
#     for i in num:
#         total += i
#     print(total)
# add(10, 20, 30, 40, 50, 60)

# def student(**datails):
#     print(datails)
#     student(name="dinga", age=20, course="python")

######kwargs#####
# def student(**details):
#     print("name:",details["name"])
#     print("age:",details["age"])
#     print("job:",details["job"])
# student(
#     name="penga",
#     age=20,
#     job="sales"
# )

######square root#####
#method1
# import math

# num = float(input("Enter a number: "))
# sqrt = math.sqrt(num)

# print("Square root =", sqrt)

#method2
# def square(num):
#     return num * num

# n = int(input("Enter a number: "))
# print("Square =", square(n))

#method3
# def square(x):
#     return x*x
# print(square(16))

# ####cube root#####
# square = lambda x:x*x
# print(square(25))

# add = lambda a,b:a+b
# print(add(10,20))

# lower_case=lambda x:x.lower()
# print(lower_case("DEEPA"))
# upper_case=lambda x:x.upper()
# print(upper_case("deepa"))

# lower_case=lambda x:x.islower()
# print(lower_case("deepa"))
# lower_case_case=lambda x:x.islower()
# print(lower_case("DEEPA")) 


# file = open("student.txt", "w")
# file.write("hello megha")
# file.close()
# print("data written successfully")

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()


# file = open("student.txt","a")
# file.write("\n uta aitha dhanu")
# file.close()
# print("data appended successfully")

# file = open("student.txt","r")
# print(file.read())
# file.close()


# try:
#     a=10
#     b=10
#     print(a/b)
# except:
#     print("something went wrong")

# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("only numbers are allowed")

# try:
#     a = int(input("Enter A: "))
#     b = int(input("Enter B: "))
#     print(a/b)
# except ZeroDivisionError:
#     print(" cannot divide by zero")
# except ValueError:
#     print("only numbers are allowed")


# try:
#     file = open("data.txt")
#     print(file.read())
# except:
#     print("file error")

# finally:
#     print("program completed")

try:
    print(10/2)
except:
    print("error")
else:
    print("success")
    
    
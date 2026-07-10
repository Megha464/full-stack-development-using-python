# # # # # # # class student:
# # # # # # #     name="penga"
# # # # # # #     def study(self):
# # # # # # #         print("penga is studying")
# # # # # # # s1=student() #s1 is object
# # # # # # # print(s1.name)
# # # # # # # s1.study() #study is method


# # # # # # class student:
# # # # # #     def details(self):
# # # # # #         print("had breakfast")
# # # # # # s1=student()
# # # # # # s1.details()
# # # # # # student.details(s1)


# # # # # class student:
# # # # #     def __init__(self,name,age): #initial is a constructor,self represents the current object
# # # # #         self.name=name
# # # # #         self.age=age
# # # # # s1=student("nandhu",20)
# # # # # s2=student("megha",21)
# # # # # s3=student("ronaldo",22)
# # # # # print(s1.name,s2.name,s3.name)
# # # # # print(s1.age,s2.age,s3.age)

# # # # class bank:
# # # #     def __init__(self ,balence):
# # # #         self.balence=balence
# # # #     def check_balence(self):
# # # #         print(self.balence)
# # # # account=bank(5000)
# # # # account.check_balence()


# # # class user:
# # #     def __init__(self,name):
# # #         self.name=name
# # #     def login(self):
# # #         print(self.name,"is logged in")
# # # u1=user("usha")
# # # u2=user("vyshu")
# # # u1.login()
# # # u2.login()

# # class father:
# #     def house(self):
# #         print("Father has a house")
# # class mother:
# #     def car(self):
# #         print("Mother has a car")
# # class son(father,mother):
# #     def bike(self):
# #         print("Son has a bike")
# # s=son()
# # s.house()
# # s.car()
# # s.bike()

# # # # # # class student:
# # # # # #     name="penga"
# # # # # #     def study(self):
# # # # # #         print("penga is studying")
# # # # # # s1=student() #s1 is object
# # # # # # print(s1.name)
# # # # # # s1.study() #study is method


# # # # # class student:
# # # # #     def details(self):
# # # # #         print("had breakfast")
# # # # # s1=student()
# # # # # s1.details()
# # # # # student.details(s1)


# # # # class student:
# # # #     def __init__(self,name,age): #initial is a constructor,self represents the current object
# # # #         self.name=name
# # # #         self.age=age
# # # # s1=student("nandhu",20)
# # # # s2=student("megha",21)
# # # # s3=student("ronaldo",22)
# # # # print(s1.name,s2.name,s3.name)
# # # # print(s1.age,s2.age,s3.age)

# # # class bank:
# # #     def __init__(self ,balence):
# # #         self.balence=balence
# # #     def check_balence(self):
# # #         print(self.balence)
# # # account=bank(5000)
# # # account.check_balence()


# # class user:
# #     def __init__(self,name):
# #         self.name=name
# #     def login(self):
# #         print(self.name,"is logged in")
# # u1=user("usha")
# # u2=user("vyshu")
# # u1.login()
# # u2.login()

# class thatha:
#     def land(self):
#         print("Thatha has land")
# class father(thatha):
#     def house(self):
#         print("Father has a house")
# class maga(father):
#     def bike(self):
#         print("Son has a bike")
# s=maga()
# s.land()
# s.house()
# s.bike()

# # # # # # class student:
# # # # # #     name="penga"
# # # # # #     def study(self):
# # # # # #         print("penga is studying")
# # # # # # s1=student() #s1 is object
# # # # # # print(s1.name)
# # # # # # s1.study() #study is method


# # # # # class student:
# # # # #     def details(self):
# # # # #         print("had breakfast")
# # # # # s1=student()
# # # # # s1.details()
# # # # # student.details(s1)


# # # # class student:
# # # #     def __init__(self,name,age): #initial is a constructor,self represents the current object
# # # #         self.name=name
# # # #         self.age=age
# # # # s1=student("nandhu",20)
# # # # s2=student("megha",21)
# # # # s3=student("ronaldo",22)
# # # # print(s1.name,s2.name,s3.name)
# # # # print(s1.age,s2.age,s3.age)

# # # class bank:
# # #     def __init__(self ,balence):
# # #         self.balence=balence
# # #     def check_balence(self):
# # #         print(self.balence)
# # # account=bank(5000)
# # # account.check_balence()


# # class user:
# #     def __init__(self,name):
# #         self.name=name
# #     def login(self):
# #         print(self.name,"is logged in")
# # u1=user("usha")
# # u2=user("vyshu")
# # u1.login()
# # u2.login()

# class father:
#     def house(self):
#         print("Father has a house")
# class mother:
#     def car(self):
#         print("Mother has a car")
# class child(father,mother):
#     def bike(self):
#         print("Son has a bike")
# s=child()
# s.house()
# s.car()
# s.bike()


#################hierarchical inheritance
class father:
    def house(self):
        print("father has a house")
class son(father):
    def bike(self):
        print("son has a bike")
class daughter(father):
    def doll(self):
        print("daughter has a doll")
obj1=son()
obj1.house()
obj1.bike()
obj2=daughter()
obj2.house()
obj2.doll()
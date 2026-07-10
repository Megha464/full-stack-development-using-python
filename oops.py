# # class student:
# #     name="penga"
# #     def study(self):
# #         print("penga is studying")
# # s1=student() #s1 is object
# # print(s1.name)
# # s1.study() #study is method


# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()
# student.details(s1)


class student:
    def __init__(self,name,age): #initial is a constructor,self represents the current object
        self.name=name
        self.age=age
s1=student("usha",20)
s2=student("vyshu",21)
s3=student("hemanth",22)
print(s1.name,s2.name,s3.name)
print(s1.age,s2.age,s3.age)


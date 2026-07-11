# # # # # # # # # class bank:
# # # # # # # # #     def __init__(self):
# # # # # # # # #         self.balance=10000
# # # # # # # # # account=bank()
# # # # # # # # # account.balance=1000000
# # # # # # # # # print(account.balance)
# # # # # # # # class bank:
# # # # # # # #     def __init__(self): 
# # # # # # # #         self._balence=10000
# # # # # # # #     def deposite(self,amount):
# # # # # # # #         self._balence+=amount
# # # # # # # #     def show_balnce(self):
# # # # # # # #             print(self._balence)

# # # # # # # # account=bank()
# # # # # # # # account.deposite(5000)
# # # # # # # # account.show_balnce()

# # # # # # # class employee:
# # # # # # #     def __init__(self,salary):
# # # # # # #         self.__salary=salary
# # # # # # #     def get_salary(self):
# # # # # # #         return self.__salary
# # # # # # # emp=employee(50000)
# # # # # # # print(emp.get_salary())

# # # # # # class employee:
# # # # # #     def __init__(self):
# # # # # #         self.__salary=0

# # # # # #     def set_salary(self, amount):
# # # # # #         if amount < 0:
# # # # # #             print("invalid salary")
# # # # # #         else:
# # # # # #             self.__salary = amount

# # # # # #     def get_salary(self):
# # # # # #         return self.__salary
# # # # # #     emp=employee()
# # # # # #     emp.set_salary(50000)
# # # # # #     print(emp.get_salary())

# # # # # ######polymorphism####
# # # # # ##polymorphism means the same method name can perform different actions depending on the object

# # # # # class dog:
# # # # #     def sound(self):
# # # # #         print("dog barks")
    
# # # # # class cat:
# # # # #     def sound(self):
# # # # #         print("cat meows")
# # # # # Dog =dog()
# # # # # Cat =cat()
# # # # # Dog.sound()
# # # # # Cat.sound()


# # # # class upi:
# # # #     def pay(self):
# # # #         print("payment done")
# # # # class creditcard:
# # # #     def pay(self):
# # # #         print("payment done")
# # # # Upi=upi()
# # # # CreditCard=creditcard()
# # # # Upi.pay()
# # # # CreditCard.pay()

# # # ###########Abstraction class ########
# # # ####abstraction means hiding internal implementation and showing only necessary features to the user

# # # from abc import ABC,abstractmethod
# # # class vehicale(ABC):
# # #     @abstractmethod
# # #     def start(self):
# # #         pass
# # # class car(vehicale):
# # #     def start(self):
# # #         print("car started")
# # # Car=car()
# # # Car.start()

# # from abc import ABC,abstractmethod
# # class dog(ABC):
# #     @abstractmethod
# #     def sound(self):
# #         pass
# # class cat(dog):
# #     def sound(self):
# #         print("cat meows")
# # class donkey(dog):
# #     def sound(self):
# #         print("donkey brays")
# # class cow(dog):
# #     def sound(self):
# #         print("cow moos")
# # Cat=cat()
# # Donkey=donkey()
# # Cow=cow()
# # Cat.sound()
# # Donkey.sound()
# # Cow.sound()

# #############
# import requests
# city=input("enter city")
# url=f"http://wttr.in/{city}?format=j1"
# response=requests.get(url)
# data=response.json()
# temp=data['current_condition'][0]['temp_C']
# print("Temperature:",temp,"°C") 
# humidity=data['current_condition'][0]['humidity']
# print("Humidity:",humidity,"%")
# condition=data['current_condition'][0]['weatherDesc'][0]['value']
# print("Condition:",condition)


##############
import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

print("\n------ Current Weather ------")
print("City:", city)
print("Temperature:", current["temp_C"], "C")
print("Humidity:", current["humidity"], "%")
print("Weather:", current["weatherDesc"][0]["value"])
print("Wind Speed:", current["windspeedKmph"], "km/h")

print("\n------ Hourly Forecast ------")

hourly = data["weather"][0]["hourly"]

for hour in hourly:
    print(
        f"Time: {hour['time']} | "
        f"Temp: {hour['tempC']}C | "
        f"Humidity: {hour['humidity']}% | "
        f"Weather: {hour['weatherDesc'][0]['value']}"
    )


import math
import time
from datetime import datetime
from typing import override

class MobilePhone:

    def __init__(self, brand, model, color, battery=75):
        print('new phone created')
        self.brand = brand
        self.model = model
        self.color = color
        self.battery = battery
        self.created_at = datetime.now()

    def ring(self):
        print(f"{self.model} is ringing")
        # print(f"{self.__str__()} is ringing")

    @override
    def __str__(self) -> str:
        # super.__str__()
        # print(self.__dict__)
        return f"mobile_phone.MobilePhone brand=[{self.brand}] model=[{self.model}] " + \
               f"color=[{self.color}] battery=[{self.color}] created_at=[{self.created_at}]" +\
               f"datetime={datetime.now().__str__()}"

    # 1. str-like
    # 2. developer-code
    def __repr__(self):
        # 1. str-like
        # worse
        # return f"mobile_phone.MobilePhone brand=[{self.brand}] model=[{self.model}] " + \
        #        f"color=[{self.color}] battery=[{self.color}] created_at=[{self.created_at}]" +\
        #        f"datetime={datetime.now().__str__()}"
        # better
        # return self.__str__()

        # 2. developer-mode i.e. save time for next time
        #    MobilePhone('Samsung', 'S25Ultra', 'black', 25)
        return f"MobilePhone('{self.brand}', '{self.model}', '{self.color}', {self.battery})"

samsung = MobilePhone('Samsung', 'S25Ultra', 'black', 25)
iphone = MobilePhone('IPhone', '16pro', 'white', 79)

iphone.ring()

print("isinstance(samsung, MobilePhone) ?", isinstance(samsung, MobilePhone))

class Person:
    def __init__(self, name: str, height: float, weight: float):
        self.name = name
        self.height = height
        self.weight = weight

    def print_name(self) -> None:
        print(f"Person name is {self.name}")

    def get_measurements(self) -> str:
        return f"Person weight is {self.weight} and height is {self.height}"

    @override
    def __str__(self):
        return f"Person {self.name} weight={self.weight} height(meter)={self.height} super={super().__str__()}"

danny = Person('danny', 1.8, 89)

print(danny.get_measurements())
danny.print_name()

print(danny)




from datetime import datetime
print("wellcome to the Interactive Persnal data Collecter! \n")

name = input("Please enter your name:")
age = int (input("Please enter your age:"))
hight = float(input("Please enter your height:"))
favorite_number = int(input("Please enter your favorite number:"))
print("\n Thank you! Here is the information we collected: \n")
print(f"Name: {name} (Type: {type(name)}, Memory Addrss:{id(name)})")
print(f"Age: {name} (Type: {type(age)}, Memory Addrss:{id(age)})")
print(f"Hight: {hight} (Type: {type(hight)}, Memory Addrss:{id(hight)})")
print(f"Favourite Number: {favorite_number} (Type: {type(favorite_number)}, Memory Addrss:{id(favorite_number)})\n")

current_year =  datetime.now().year
birth_year = current_year - age
print(f"Your birth year is approximately:{birth_year}"
      f"(based on your age of {age})")
print("\n Thank you for using the Personal Data Collector. Goodbye!")

import datetime

name=input("enter your name: ")
age=int(input("enter your age: "))
year=datetime.datetime.today().year
birth_year=(year-age)
cent_age=birth_year+100

print(f"hey {name} ! you will turn 100 in the year {cent_age} ")
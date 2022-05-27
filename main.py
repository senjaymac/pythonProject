# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

print(5)
print("Hello World")
print("\n")

print("There was once a pilot who loved adventure")
print("There pilot would take her plane to unknown places.")
print("She brings home alot of fruits.")
print("Then she goes home to her pet lion, Chuckles.")
print("\n\n\n")


character_Job = "Pirate"
character_Ride = "Ship"
character_Souvenir = "Gold"
character_Pet = "Parrot"


print("There was once a "+ character_Job +" who loved adventure")
print("There pilot would take her "+ character_Ride +" to unknown places.")
print("She brings home alot of "+ character_Souvenir +".")
print("Then she goes home to her pet "+ character_Pet +", Chuckles.")
print("\n\n\n")
# test comment

#1.16 coding challenge
string = "Sample String"
print(string)
print("\n\n\n")

print("I could use a cup of coffee \n \n")

favorite_Book = "Slaughterhouse-Five"
least_favorite_Book = "Jane Eyre"

print("I enjoyed reading "+ least_favorite_Book +". \n \n")

w = "Cats"
x = 10
y = "Fish"
z = 9

print(w)
print(z)
print("\n\n\n")

# Module 2

def nice_day(name):
    print("Have a nice day "+ name +"!")

nice_day("Senon")
print("\n\n\n")

# coding exercise 2.7

name = input("Enter your Name: ")
age = input("Your Age: ")
favorite_color = input("Enter your favorite color: ")
favorite_movie = input("Enter your favorite movie: ")
mobile_number = input("Enter your mobile number: ")
motto_in_life = input("Enter your motto in life: ")
print("\n\n\n")

print(10 > 7)
print(str(73911))
print(tuple("Thank God its Friday!"))
print(float(4302))
print(int(3299.35640))
print("\n\n\n")


class Customers:
    greeting = "Welcome to Coffee Palace!"

c_1 = Customers()
c_1.name = "Samirah"
c_1.beverage = "Iced Cofee Latte"
c_1.food = "Cinnamon Roll"
c_1.total = 225

c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "Caramel Macchiato"
c_2.food = "Glazed Doughnut"
c_2.total = 230

print(Customers.greeting)
print(c_1.beverage)
print(c_2.food)
print("\n\n\n")


# 3.8 coding exer

print(217 * 6)
print(600+35234)
print(67/12)
print(56329%982)
print(34**5)
print("\n\n\n")


my_age = 22
mom_age = 61
sister_age = 29

print(mom_age < sister_age and my_age == 22)
print(mom_age == 61)
print(mom_age > 34 or sister_age == 22)
print(mom_age >= 54)
print(not(sister_age <= 400 and my_age == 22))
print("\n\n\n")

x = 332
y = 2031
if x >= y:
    print("x is greater than or equal to y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")


# iterrations and loops

furniture = ["table", "chair", "cabinet", "desk", "couch"]
for x in furniture:
    if x == "cabinet":
        continue
    print(x)
print("\n\n\n")

i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")




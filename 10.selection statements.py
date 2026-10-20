#nested if-else
A=input("Enter wht day is today - ")
is_raining = (input("is it raining(true/false) - "))
if A == "sunday" or A== "saturday":
    if is_raining == "true":
        print("lets not go - it's raining")
    else:
        print("letttt'ssss gooooo")
else:
    print("It's weekday, let's wait until weekend")

#OR
print("-----------------------------------------------------------------------------------")

A=input("Enter wht day is today - ")
is_raining = (input("is it raining(True/False) - "))
is_raining = is_raining.strip().capitalize()
if A == "sunday" or A== "saturday":
    if is_raining == "True": #bool data type
        print("lets not go - it's raining")
    else:
        print("letttt'ssss gooooo")
else:
    print("It's weekday, let's wait until weekend")



#match-case statements
a=input("Enter the today's day of a week = ")
match a:
    case "monday":
        print('a start of a week')
    case "monday":
        print('very bad day because it is monday')
    case "friday":
        print("End of weekdays")
    case "sunday" | "sunday":
        print("it'ss weekenddd!!")
    case _:
        print("nothing")

#bus pass eligibility
gender=input("Enter your Gender = ")
age=int(input("Enter Your Age = "))
if gender=="female":
    print("Your bus pass is free")
else:
    if age<=5:
        print("bus pass is free")
    elif age>=60:
        print("you get senior citizen discount for bus pass")
    else:
        print("Pay the full price")


#library eligibility membership
age=int(input("Enter your age = "))
if age<=18:
    print("u get student membership")
elif age>=60:
    print("u get senior citizen membership")
else:
    print("u get regular membership")

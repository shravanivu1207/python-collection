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
    if is_raining == "True":
        print("lets not go - it's raining")
    else:
        print("letttt'ssss gooooo")
else:
    print("It's weekday, let's wait until weekend")
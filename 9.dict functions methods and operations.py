#creating dictionary
birthday={
    "shravani" : "09-05-2007",
    "IDIOT" : "28-11-2007",
    "dosa" : "Ramwesharam",
    "bisi bele bath" : "naidu"
}
print(birthday)

#acessing dictionary values
print(birthday["shravani"])

#using get() which is safer because it doesn’t throw an error if the key doesn’t exist.
print(birthday.get("IDIOT","not found"))
print(birthday.get("no-one","not found"))

#adding and updating value
birthday["Ratan Tata"] = "28-12-1937"
print(birthday)
birthday["IDIOT"]="28-11-2006" #updating
print(birthday)

#pop() Here, we can store the value of the key which is going to be poped.
Canteen_name = birthday.pop("dosa")
print(birthday)
print(Canteen_name)

#del()
del birthday["bisi bele bath"]
print(birthday)

#clear
birthday.clear()
print(birthday)

#dictionary Methods
birthday={
    "Ratan Tata" : "28-11-1937",
    "shravani" : "09-05-2007",
    "IDIOT" : "28-11-2007",
}

#keys()
print(birthday.keys())

#values
print(birthday.values())

#items()
print(birthday.items())

#update() create new dictionary and merge it
a={"Nothing" : "IDK"}
birthday.update(a)
print(birthday)

#creating a dictionary with different data types
a={
    2 : "it is number",
    "Good Morning" : "kind greeting",
    12.6 : "it is float",
    (2,4,"hello") : "example of tuple",
    "friends" : ["xyz","abc","pqr"] #we cannot put list,sets as key in dictionary because lists,sets are mutuable. but we can use lists,sets has values
}
print(a)
print(type(a))

#adding 2 values in dictionary
item1 = {
    "name" : "Sugar",
    "weight" : 3
}
item2 = {
    "name" : "coffee",
    "weight"  : 1
}
print(f"total weight : {item1["weight"] + item2["weight"]}kg")

items=[item1,item2]
print(items)

birthday={
    "Ratan Tata" : '28-12-1937',
    "IDIOT" : "28-11-2007",
    "shravani" : "09-05-2007"
}
a=birthday.copy() #copy()
print(a)

birthday.popitem() #popitem()
print(birthday)

# creating dict using function "dict()"
a = dict(name = "xyz", age=20)
print(a)
print(type(a))

#creating list of dict
a=[
 {
    "hello" : "greeting",
      2 : "number"
 },
{
 "hi" : "greeting",
 10.9 : "float value"
}
]
print(a)
# adding 2 values by creating list of dicts
items=[
    {
    "name" : "Sugar",
    "weight" : 3
    },
    {"name" : "coffee",
        "weight"  : 1
    }
]
print(f"Total weight = {items[0]["weight"] + items[1]["weight"]}kg")
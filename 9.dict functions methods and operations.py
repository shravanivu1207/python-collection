#creating dictionary
birthday={
    "shravani" : "09-05-2007",
    "IDIOT" : "28-11-2007"
}
print(birthday)

#acessing dictionary values
print(birthday["shravani"])

#using get() which is safer because it doesn’t throw an error if the key doesn’t exist.
print(birthday.get("IDIOT","not found"))
print(birthday.get("no-one","not found"))


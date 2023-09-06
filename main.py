# write your code here
person = {
    "name": "FARAH",
    "age": 21,
    "hobbies": ["Football, swimming, singing"]
}
print(person["name"])
print(person["age"])
person["age"] = 22
print(person["age"])
person["country"] = "UK"
print(person)
print(len(person))
person["hobbies"] = "drawing"
print(person)


def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW YOU ARE AMAZ")
    else:
        print("Oops")


check_hobbies(person)

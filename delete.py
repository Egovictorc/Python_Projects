age = 5

def calcAge(yearOfBirth):
    #global age
    y = globals()["age"]
    age = 2022 - yearOfBirth
    print(age)


calcAge(2000)
print(age)
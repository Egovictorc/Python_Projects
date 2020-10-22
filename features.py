x = {
    "name": "uche",
    "age": 5,
    "city": "onitsha"
}

y = {
    "school": "dmgs",
    "state": "Onitsha",
    "country": "Nigeria"
}

#z = x | y
#print(z)

y |= x
print(y)

name = "aaaaaaaaaaaaaaaaaauche"

print(name)
print(name.removeprefix("a"))
info =  "three cool features in python"
print(info.rstrip("python"))
print(info.removesuffix("python"))

import math
print(math.lcm(3,5, 10))
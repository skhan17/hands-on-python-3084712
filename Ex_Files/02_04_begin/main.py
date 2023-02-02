NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1
#John 20
#Paul 21
#George 22
#Ringo 23

for name in NAMES:
    print(name)
# John
# Paul
# George
# Ringo

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")
# John 20
# Paul 21
# George 22
# Ringo 23

for name in reversed(NAMES):
    print(name)
# Ringo
# George
# Paul
# John

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
# 0 John
# 1 Paul
# 2 George
# 3 Ringo

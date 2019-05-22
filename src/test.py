import random

sabbat = random.randint(1, 7)
print(sabbat)

lion = []
cat = []

for i in range(1, 8):
    if i == sabbat:
        continue
    rand = random.randint(1, 2)
    if (rand == 1 and len(lion) < 3) or len(cat) >= 3:
        lion.append(i)
    elif (rand == 2 and len(cat) < 3) or len(lion) >= 3:
        cat.append(i)

print("lion days:", lion)
print("cat days:", cat)
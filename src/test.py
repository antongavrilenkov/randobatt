import random

shabbat = 7

lion = []
cat = []

for i in range(1, 8):
    if i == shabbat:
        continue
    rand = random.randint(1, 2)
    if (rand == 1 and len(lion) < 3) or len(cat) >= 3:
        lion.append(i)
    elif (rand == 2 and len(cat) < 3) or len(lion) >= 3:
        cat.append(i)

print("lion days:", lion)
print("cat days:", cat)
print("shabbat", shabbat)
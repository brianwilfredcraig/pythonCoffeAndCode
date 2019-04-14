aList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
for item in aList:
  if (int(item) < 5):
    newList.append(item)


for item2 in newList:
    print(item2)

print([item3 for item3 in aList if item3 < 5])
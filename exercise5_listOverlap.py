a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


theListToIterateOn =a
theListToTestAgainst = b

overLapList = []
for item in theListToIterateOn:
    if (item in theListToTestAgainst):
        overLapList.append(item)

print(overLapList)

commonList = set()
[commonList.add(x) for x in a for y in b if x == y]
print(list(commonList))
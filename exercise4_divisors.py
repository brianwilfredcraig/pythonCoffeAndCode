theNumber = int(input("Enter a number to get divisors: "))
testNumber = 1
divisorList = []
while testNumber < theNumber:
    if ((theNumber % testNumber) == 0):
      divisorList.append(testNumber)
    testNumber = testNumber + 1
    
print(divisorList)
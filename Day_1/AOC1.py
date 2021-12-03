# 9:01:71

f = open("AOC1Buk.txt", "r")
lines = f.readlines()

increaseCounter = 0
decreaseCounter = 0
previousValue = 0

threeMeasurementWindow = []
counter = 3
tempValue = 0
tempCounter = 0

for i, line in enumerate(lines):
    line = int(line)
    if i != 0:
        if (line - previousValue) > 0:
            increaseCounter += 1
        else:
            decreaseCounter += 1
    previousValue = line


print("Increase Counter 1:", increaseCounter)
increaseCounter = 0
decreaseCounter = 0
previousValue = 0


for i, line_i in enumerate(lines):
    tempCounter = i
    for j, line_j in enumerate(lines):
        if j >= tempCounter and counter != 0:
            tempValue += int(line_j)
            counter -= 1
        elif counter == 0:
            threeMeasurementWindow.append(tempValue)
            tempValue = 0
            counter = 3
            break

print("Three Measurement Window:", threeMeasurementWindow)

for i, line in enumerate(threeMeasurementWindow):
    line = int(line)
    if i != 0:
        if (line - previousValue) > 0:
            increaseCounter += 1
        else:
            decreaseCounter += 1
    previousValue = line


print("Increase Counter 2:", increaseCounter)

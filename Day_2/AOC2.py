# 5:37:65
horizontalPos = 0
depth = 0


def addHorizontal(tempNum: int):
    global horizontalPos
    horizontalPos += tempNum

def minusDepth(tempNum):
    global depth
    depth -= tempNum

def addDepth(tempNum):
    global depth
    depth += tempNum


caseOperator = {
    "forward": addHorizontal,
    "up": minusDepth,
    "down": addDepth
}


f = open("AOCI2.txt", "r")
lines = f.readlines()


for i, line in enumerate(lines):
    inputData = line.split(" ")
    instruction, tempNum = inputData[0], int(inputData[1])
    caseOperator[instruction](tempNum)


print("horizontal position:", horizontalPos, "depth:", depth, "multiply:", horizontalPos*depth)

# 7:09:09

horizontalPos = 0
depth = 0
aim = 0


def addHorizontal(tempNum: int):
    global horizontalPos, depth, aim
    horizontalPos += tempNum
    depth += aim * tempNum

def minusDepth(tempNum):
    global aim
    aim -= tempNum

def addDepth(tempNum):
    global aim
    aim += tempNum

caseOperator = {
    "forward": addHorizontal,
    "up": minusDepth,
    "down": addDepth
}

for i, line in enumerate(lines):
    inputData = line.split(" ")
    instruction, tempNum = inputData[0], int(inputData[1])
    caseOperator[instruction](tempNum)


print("horizontal position:", horizontalPos, "depth:", depth, "multiply:", horizontalPos*depth)



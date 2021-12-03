f = open("AOCI3.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]


bitList = {}

# Part 1
def create_bit_list(line: str):
    # {b0:{"0": , "1": }}
    global bitList
    for i, bit in enumerate(line):
        key = f'{"b"}{i}'
        if key in bitList.keys():
            bitList[key][bit] += 1
        else:
            bitList[key] = {
                "0": 0, "1": 0
            }
            bitList[key][bit] = 1


def bit_calculator(bits: dict):
    gamma_temp = ""
    epsilon_temp = ""

    for value in bits.values():
        a, b = value.values()
        if a > b:
            gamma_temp += "0"
            epsilon_temp += "1"
        else:
            gamma_temp += "1"
            epsilon_temp += "0"

    return [int(gamma_temp, 2), int(epsilon_temp, 2)]


for line in lines:
    create_bit_list(line)

gamma, epsilon = bit_calculator(bitList)
print("Power Consumption:", gamma * epsilon)

# Part 2
def life_support_calculator(lines):
    generator = lines.copy()
    scrubber = lines.copy()
    bitLength = len(lines[0])
    for i in range(bitLength):
        if len(generator) > 1:
            a = len([x for x in generator if x[i] == "0"])
            b = len([x for x in generator if x[i] == "1"])
            if a > b:
                generator = [x for x in generator if x[i] == "0"]
            else:
                generator = [x for x in generator if x[i] == "1"]
        if len(scrubber) > 1:
            a1 = len([x for x in scrubber if x[i] == "0"])
            b1 = len([x for x in scrubber if x[i] == "1"])
            if a1 > b1:
                scrubber = [x for x in scrubber if x[i] == "1"]
            else:
                scrubber = [x for x in scrubber if x[i] == "0"]

    return [int(generator[0], 2), int(scrubber[0], 2)]


generator, scrubber = life_support_calculator(lines)

print("Life Support:", generator * scrubber)


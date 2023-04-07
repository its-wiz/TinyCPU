binary_file = open("LogicEmulation/sample.asm", "r")
lines = [line.strip() for line in binary_file.readlines()]
src = [item.split(",") for item in lines]

SYNTAX = {
    "MOV": "0000000000000001",
    "RAM_WRITE": "0000000000000010",
    "RAM_WRITE_REG": "0000000000000011",
    "RAM_READ": "0000000000000100"
}

REGISTERS = {
    "A": "0000000000000001",
    "B": "0000000000000010",
    "C": "0000000000000011",
    "D": "0000000000000100"
}

file = open("LogicEmulation/sample.binary", "w")

for line in src:
    opcode = line[0]
    operand_1 = line[1][1::]
    operand_2 = line[2][1::]
    if opcode in SYNTAX:
        file.write(SYNTAX[opcode] + "\n")
    if operand_1 in REGISTERS:
        file.write(REGISTERS[operand_1] + "\n")

    if operand_1.isnumeric():
        binary = str(bin(int(operand_1))[2:])
        while len(binary) <= 15:
            binary = "".join(("0", binary))
        file.write(binary + "\n")

    if operand_2 in REGISTERS:
        file.write(REGISTERS[operand_2] + "\n")
    if operand_2.isnumeric():
        binary = str(bin(int(operand_2))[2:])
        while len(binary) <= 15:
            binary = "".join(("0", binary))
        file.write(binary + "\n")
    
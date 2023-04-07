import LogicEngine
import time

MEGA_BYTE = 8388608
clock = LogicEngine.Clock()

test_ram = LogicEngine.Ram(1024,16)

binary_file = open("LogicEmulation/sample.binary", "r")
lines = [line.strip() for line in binary_file.readlines()]
count = 0
for binary in lines:
    li = []
    for item in binary:
        print(item)
        li.append(int(item))
    test_ram.WriteSequenceToRam(count, li)
    count += 1
    
gen_ram = LogicEngine.Ram(1024, 16) # General Purpose RAM

decode_reg_1 = LogicEngine.Register()
decode_reg_2 = LogicEngine.Register()
decode_reg_3 = LogicEngine.Register()

reg_A = LogicEngine.Register()
reg_B = LogicEngine.Register()
reg_C = LogicEngine.Register()
reg_D = LogicEngine.Register()

def ExecuteMOV_REG_A(): reg_A.write(decode_reg_3.read())
def ExecuteMOV_REG_B(): reg_B.write(decode_reg_3.read())
def ExecuteMOV_REG_C(): reg_C.write(decode_reg_3.read())
def ExecuteMOV_REG_D(): reg_D.write(decode_reg_3.read())

def PreformMOVInstruction(): # MOV [REG] [VALUE]
    clock.tick()
    print("HERE AT MOV INSTRUCTION")
    decode_reg_2.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()    
    decode_reg_3.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()
    print(f"OPCODE: {decode_reg_1.read()}")
    print(f"OPERAND: {decode_reg_2.read()}")
    print(f"OPERAND: {decode_reg_3.read()}")
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_2.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), ExecuteMOV_REG_A) # REG A
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_2.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), ExecuteMOV_REG_B) # REG B
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_2.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), ExecuteMOV_REG_C) # REG C
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_2.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), ExecuteMOV_REG_D) # REG D

def ExecuteRAM_WRITE(): gen_ram.WriteSequenceToRam(LogicEngine.SequenceConversion(decode_reg_2.read()), decode_reg_3.read())

def Preform_RAM_WRITE_Instruction(): # RAM_WRITE [LOC] [VALUE]
    clock.tick()
    decode_reg_2.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()    
    decode_reg_3.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()
    # print(f"OPCODE: {decode_reg_1.read()}")
    # print(f"OPERAND: {decode_reg_2.read()}")
    # print(f"OPERAND: {decode_reg_3.read()}")
    ExecuteRAM_WRITE()

def ExecuteRAM_WRITE_REG_A(): gen_ram.WriteSequenceToRam(LogicEngine.SequenceConversion(decode_reg_2.read()), reg_A.read())
def ExecuteRAM_WRITE_REG_B(): gen_ram.WriteSequenceToRam(LogicEngine.SequenceConversion(decode_reg_2.read()), reg_B.read())
def ExecuteRAM_WRITE_REG_C(): gen_ram.WriteSequenceToRam(LogicEngine.SequenceConversion(decode_reg_2.read()), reg_C.read())
def ExecuteRAM_WRITE_REG_D(): gen_ram.WriteSequenceToRam(LogicEngine.SequenceConversion(decode_reg_2.read()), reg_D.read())

def Preform_RAM_WRITE_REG_Instruction(): # RAM_WRITE [LOC] [REGISTER-ID]
    clock.tick()
    decode_reg_2.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()    
    decode_reg_3.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), ExecuteRAM_WRITE_REG_A) # REG A
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), ExecuteRAM_WRITE_REG_B) # REG B
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), ExecuteRAM_WRITE_REG_C) # REG C
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), ExecuteRAM_WRITE_REG_D) # REG D
    print(f"OPCODE: {decode_reg_1.read()}")
    print(f"OPERAND: {decode_reg_2.read()}")
    print(f"OPERAND: {decode_reg_3.read()}")

def ExecuteRAM_READ_REG_A(): reg_A.write(gen_ram.ReadSequenceFromRam(LogicEngine.SequenceConversion(decode_reg_2.read())))
def ExecuteRAM_READ_REG_B():
    print("Here writing to B") 
    reg_B.write(gen_ram.ReadSequenceFromRam(LogicEngine.SequenceConversion(decode_reg_2.read())))
def ExecuteRAM_READ_REG_C(): reg_C.write(gen_ram.ReadSequenceFromRam(LogicEngine.SequenceConversion(decode_reg_2.read())))
def ExecuteRAM_READ_REG_D(): reg_D.write(gen_ram.ReadSequenceFromRam(LogicEngine.SequenceConversion(decode_reg_2.read())))

def Preform_RAM_READ_Instruction(): # RAM_READ [REGISTER-ID] [LOC]
    print("RAM READING!!")
    clock.tick()
    decode_reg_2.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()    
    decode_reg_3.write(test_ram.ReadSequenceFromRam(clock.count))
    clock.tick()
    print(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]))
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), ExecuteRAM_READ_REG_A) # REG A
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), ExecuteRAM_READ_REG_B) # REG B
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), ExecuteRAM_READ_REG_C) # REG C
    LogicEngine.Connector(LogicEngine.SequenceComparison(decode_reg_3.read(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), ExecuteRAM_READ_REG_D) # REG D  

instructions = 3
while True:
    current_ram_sequence = test_ram.ReadSequenceFromRam(clock.count)
    LogicEngine.Connector(LogicEngine.SequenceComparison(current_ram_sequence, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]), PreformMOVInstruction) # If Sequence is the MOV Instruction.
    LogicEngine.Connector(LogicEngine.SequenceComparison(current_ram_sequence, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]), Preform_RAM_WRITE_Instruction) # If Sequence is the RAM_WRITE Instruction.
    LogicEngine.Connector(LogicEngine.SequenceComparison(current_ram_sequence, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]), Preform_RAM_WRITE_REG_Instruction) # If Sequence is the RAM_WRITE_REG Instruction.
    LogicEngine.Connector(LogicEngine.SequenceComparison(current_ram_sequence, [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]), Preform_RAM_READ_Instruction)
    if clock.count == instructions * 3: break

# MOV 2, 1
print("\tAnalytics\t")
print("RAM Value:")
print(test_ram.ram)

print("Decode Reg 1 Value:")
print(decode_reg_1.read())
print("Decode Reg 2 Value:")
print(decode_reg_2.read())
print("Decode Reg 3 Value:")
print(decode_reg_3.read())

print("Reg A Value:")
print(reg_A.read())

print("Reg B Value:")
print(reg_B.read())

print("Reg C Value:")
print(reg_C.read())

print("General Purpose RAM Value:")
print(gen_ram.ram)
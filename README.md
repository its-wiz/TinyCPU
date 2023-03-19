# TinyCPU
 Custom Architecture CPU Logic Design.
 Built in Emulator.
 Built in Assembler.
 Built in Logic Engine to simulate the CPU.
 16 ( x 3 ) Bits Per Instruction containing the following:
 Instruction
 Operand 1
 Operand 2

 Binary ->
 
 Currently Supports Basic Instructions Such As:
 Instructions:
     "MOV": "0000000000000001"
     "RAM_WRITE": "0000000000000010"
     "RAM_WRITE_REG": "0000000000000011"
     "RAM_READ": "0000000000000100"

 Currently Contains The Following Registers:
 Registers:
     "A": "0000000000000001" -> 1
     "B": "0000000000000010" -> 2
     "C": "0000000000000011" -> 3
     "D": "0000000000000100" -> 4
 Assembley Equivalent: 
 MOV, [REGISTER], [VALUE]
 RAM_WRITE, [LOCATION], [VALUE]
 RAM_WRITE_REG, [LOCATION], [REGISTER]
 RAM_READ, [LOCATION], [REGISTER] 

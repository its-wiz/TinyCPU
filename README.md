# TinyCPU
 > -  Custom Architecture CPU Logic Design.<br />
 > - Built in Emulator.<br />
 > - Built in Assembler.<br />
  - Built in Logic Engine to simulate the CPU.<br />
 16 ( x 3 ) Bits Per Instruction containing the following:<br />
 Instruction<br />
 Operand 1<br />
 Operand 2<br />
 <br />
 Currently Supports Basic Instructions Such As:<br />
 | Instructions: | <br />
     "MOV": "0000000000000001"<br />
     "RAM_WRITE": "0000000000000010"<br />
     "RAM_WRITE_REG": "0000000000000011"<br />
     "RAM_READ": "0000000000000100"<br />
<br />
 Currently Contains The Following Registers:<br />
 | Registers: | <br />
     "A": "0000000000000001" -> 1<br />
     "B": "0000000000000010" -> 2<br />
     "C": "0000000000000011" -> 3<br />
     "D": "0000000000000100" -> 4<br />
<br />
 | Assembley Equivalent: | <br />
 MOV, [REGISTER], [VALUE]<br />
 RAM_WRITE, [LOCATION], [VALUE]<br />
 RAM_WRITE_REG, [LOCATION], [REGISTER]<br />
 RAM_READ, [LOCATION], [REGISTER] <br />

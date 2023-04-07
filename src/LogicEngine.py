# Copyright 2023 emir
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
def BoolToBit(bool):
    if bool == True: return 1
    return 0

def NOT(bit):
    if bit == 0: return 1
    return 0

def AND(bit2,bit1):
    return BoolToBit(bit2 == 1 and bit1 == 1)

def OR(bit2,bit1):
    return BoolToBit(bit2 == 1 or bit1 == 1)

class Clock():
    def __init__(self) -> None:
        self.count = 0
    def tick(self): 
        print(f"Tick no.{self.count}")
        self.count = self.count + 1

class Ram():
    def __init__(self, size, chunking) -> None:
        self.ram = [0 for _ in range(size)]
        self.chunking = chunking
    def WriteToRam(self, loc, toWrite):
        self.ram[loc] = toWrite
    def WriteSequenceToRam(self, loc, sequence):
        loc = loc * self.chunking
        for x in range(len(sequence)):
            self.ram[loc + x] = sequence[x]
    def ReadSequenceFromRam(self, loc):
        loc = loc * self.chunking
        sequence = []
        for x in range(self.chunking):
            sequence.append(self.ram[loc + x])
        return sequence
    def ReadFromRam(self, loc):
        return self.ram[loc]

def SequenceComparison(seq1, seq2):
    return BoolToBit(seq1 == seq2)

def SequenceConversion(binary):
    print(int(''.join(str(val) for val in binary), 2))
    return int(''.join(str(val) for val in binary), 2)

def Connector(condition, func):
    if condition == 1: func()

class Register():
    def __init__(self) -> None:
        self.sequence = []
    def read(self):
        return self.sequence
    def write(self, seq):
        self.sequence = seq
import time
from typing import Union

class ALU:

    def __init__(self):
        self.variables = {"w": 0, "x": 0, "y": 0, "z": 0}

    def input(self, variable: str, value: int):
        self.variables[variable] = value
    
    def add(self, variable: str, other: str):
        if other in self.variables:
            self.variables[variable] += self.variables[other]
        else:
            self.variables[variable] += int(other)
    
    def mul(self, variable: str, other: str):
        if other in self.variables:
            self.variables[variable] *= self.variables[other]
        else:
            self.variables[variable] *= int(other)
    
    def div(self, variable: str, other: str):
        if other in self.variables:
            self.variables[variable] = int(self.variables[variable] / self.variables[other]) 
        else:
            self.variables[variable] = int(self.variables[variable] / int(other))

    def mod(self, variable: str, other: str):
        if other in self.variables:
            self.variables[variable] %= self.variables[other]
        else:
            self.variables[variable] %= int(other)

    def eql(self, variable: str, other: str):
        if other in self.variables:
            self.variables[variable] = 1 if self.variables[variable] == self.variables[other] else 0
        else:
            self.variables[variable] = 1 if self.variables[variable] == int(other) else 0

    def __str__(self):
        return str(self.variables)

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    program = raw_data.split("\n")
    for line in program:
        if line[4] == "y":
            print(line)
    """
    for i in range(99_999_999_999_999, 9_999_999_999_999, -1):
        print(i)
        myALU = ALU()
        inputs = [int(j) for j in str(i)]
        run_program(myALU, program, inputs)
        if myALU.variables["z"] == 0:
            print(f"Part 1: {i}")
    """
def run_program(myALU: ALU, program: list, inputs: list) -> None:
    for command in program:
        if "inp" in command:
            myALU.input(command[4], inputs.pop(0))
        elif "add" in command:
            myALU.add(command[4], command[6:])
        elif "mul" in command:
            myALU.mul(command[4], command[6:])
        elif "div" in command:
            myALU.div(command[4], command[6:])
        elif "mod" in command:
            myALU.mod(command[4], command[6:])
        elif "eql" in command:
            myALU.eql(command[4], command[6:])    

if __name__ == "__main__":
    print(run_script("input.txt"))
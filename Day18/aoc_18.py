import time
from typing import Union

class SnailfishNumber:

    def __init__(self, other = None):
        if other == None:
            self.depth = []
            self.values = []
        else:
            self.depth = list(other.depth)
            self.values = list(other.values)

    def is_valid(self):
        for depth in self.depth:
            if depth >= 5:
                return False
        for value in self.values:
            if value >= 10:
                return False
        return True

    def reduce(self):
        while not self.is_valid():
            explosion = False
            for i in range(len(self.depth)):
                if self.depth[i] >= 5:
                    self.explode(i)
                    explosion = True
                    break
            if explosion:
                continue
            for i in range(len(self.values)):
                if self.values[i] >= 10:
                    self.split(i)
                    break

    def add(self, other):
        new_depth = []
        new_values = []
        for i in range(len(self.depth)):
            new_depth.append(self.depth[i] + 1)
            new_values.append(self.values[i])
        for i in range(len(other.depth)):
            new_depth.append(other.depth[i] + 1)
            new_values.append(other.values[i])
        self.depth = new_depth
        self.values = new_values

    def explode(self, invalid_idx: int):
        if self.depth[invalid_idx + 1] < 5:
            print(f"Issue exploding {str(self)}, invalid index {invalid_idx}")
        if invalid_idx == 0:
            self.values.pop(0)
            self.depth.pop(0)
            self.depth[0] -= 1
            self.values[1] += self.values[0]
            self.values[0] = 0
        elif invalid_idx == len(self.depth) - 2:
            self.values.pop()
            self.depth.pop()
            self.depth[-1] -= 1
            self.values[-2] += self.values[-1]
            self.values[-1] = 0
        else:
            self.values[invalid_idx - 1] += self.values[invalid_idx]
            self.values[invalid_idx + 2] += self.values[invalid_idx + 1]
            self.values.pop(invalid_idx)
            self.depth.pop(invalid_idx)
            self.values[invalid_idx] = 0
            self.depth[invalid_idx] -= 1
        
    def split(self, invalid_idx: int):
        half_down = self.values[invalid_idx] // 2
        if self.values[invalid_idx] % 2 == 1:
            self.values[invalid_idx] = half_down + 1
        else:
            self.values[invalid_idx] = half_down
        self.values.insert(invalid_idx, half_down)
        self.depth[invalid_idx] += 1
        self.depth.insert(invalid_idx, self.depth[invalid_idx])
        if len(self.depth) != len(self.values):
            print("Bug in split function")

    def magnitude(self) -> int:
        magnitude_depth = list(self.depth)
        magnitudes = list(self.values)
        while len(magnitudes) > 1:
            max_depth = max(magnitude_depth)
            for i in range(len(magnitude_depth)):
                if magnitude_depth[i] == max_depth:
                    magnitudes[i] = 3 * magnitudes[i] + 2 * magnitudes.pop(i + 1)
                    magnitude_depth[i] -= 1
                    magnitude_depth.pop(i + 1)
                    break
        return magnitudes[0]

    def __str__(self):
        return str(self.depth) + "\n" + str(self.values)

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
    snailfish_numbers = []
    for raw_number in raw_data.split("\n"):
        snailfish_numbers.append(parse_snailfish_number(raw_number))
    current_number = SnailfishNumber(snailfish_numbers[0])
    for i in range(1, len(snailfish_numbers)):
        current_number.add(snailfish_numbers[i])
        current_number.reduce()
    print(f"Part 1: {current_number.magnitude()}")
    max_magnitude = 0
    for a in snailfish_numbers:
        for b in snailfish_numbers:
            if b is a:
                continue
            test = SnailfishNumber(a)
            test.add(b)
            test.reduce()
            candidate = test.magnitude()
            if candidate > max_magnitude:
                max_magnitude = candidate
    print(f"Part 2: {max_magnitude}")


def parse_snailfish_number(raw_number: str):
    depth = 0
    number_buffer = ""
    number = SnailfishNumber()
    for c in raw_number:
        if c == "[":
            depth += 1
        elif c.isnumeric():
            number_buffer += c
        elif c == ",":
            if number_buffer:
                number.depth.append(depth)
                number.values.append(int(number_buffer))
                number_buffer = ""
        elif c == "]":
            if number_buffer:
                number.depth.append(depth)
                number.values.append(int(number_buffer))
                number_buffer = ""
            depth -= 1
    return number

if __name__ == "__main__":
    print(run_script("input.txt"))
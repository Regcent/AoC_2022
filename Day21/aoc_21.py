import time
from typing import Union

class DiracDice:

    def __init__(self, p1_pos: int, p2_pos: int, p1_score: int, p2_score: int, p1_next: bool):
        self.p1_pos = p1_pos
        self.p2_pos = p2_pos
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.p1_next = p1_next

    def advance(self, value: int):
        if self.p1_next:
            self.p1_pos += value
            if self.p1_pos > 10:
                self.p1_pos -= 10
            self.p1_score += self.p1_pos
            self.p1_next = False    
        else:
            self.p2_pos += value
            if self.p2_pos > 10:
                self.p2_pos -= 10
            self.p2_score += self.p2_pos
            self.p1_next = True        
    
    def copy(self):
        return DiracDice(self.p1_pos, self.p2_pos, self.p1_score, self.p2_score, self.p1_next)

    def game_code(self) -> int:
        return self.p1_score * 22 + self. p1_pos * 484 + self.p2_score * 10648 + self.p2_pos * 234256

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
    lines = raw_data.split("\n")
    p1_pos = int(lines[0][-2:])
    p2_pos = int(lines[1][-2:])
    print(f"Part 1: {part_one(p1_pos, p2_pos)}")
    print(f"Part 2: {part_two(p1_pos, p2_pos)}")

def part_one(p1_pos: int, p2_pos: int) -> int:
    dice = 1
    turn_count = 0
    game = DiracDice(p1_pos, p2_pos, 0, 0, True)
    while game.p1_score < 1000 and game.p2_score < 1000: 
        game.advance((dice * 3 + 3) % 10)
        turn_count += 1
        dice += 3
        if dice >= 10:
            dice = dice - 10
    if game.p1_score >= 1000:
        return game.p2_score * turn_count * 3
    else:
        return game.p1_score * turn_count * 3

def part_two(p1_pos: int, p2_pos: int) -> int:
    initial_game = DiracDice(p1_pos, p2_pos, 0, 0, True)
    to_resolve = {initial_game.game_code() : [initial_game, 1]}
    wins_p1 = 0
    wins_p2 = 0
    count = 0
    while to_resolve:
        new_games = {}
        for game_code in to_resolve:         
            if to_resolve[game_code][0].p1_score >= 21:
                wins_p1 = wins_p1 + to_resolve[game_code][1]
                continue
            if to_resolve[game_code][0].p2_score >= 21:
                wins_p2 = wins_p2 + to_resolve[game_code][1]
                continue
            occurrences = [1, 3, 6, 7, 6, 3, 1]
            for i in range(len(occurrences)):
                new_game = to_resolve[game_code][0].copy()
                new_game.advance(i + 3)
                if new_game.game_code() not in new_games:
                    new_games[new_game.game_code()] = [new_game, to_resolve[game_code][1] * occurrences[i]]
                else:
                    new_games[new_game.game_code()][1] += to_resolve[game_code][1] * occurrences[i]
        to_resolve = new_games
    print(wins_p1, wins_p2)
    return max(wins_p1, wins_p2)

if __name__ == "__main__":
    print(run_script("input.txt"))

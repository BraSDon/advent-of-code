from enum import Enum
from typing import Self, List, Tuple


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    @staticmethod
    def from_string(s: str) -> Self:
        match s:
            case "X":
                return Result.LOSS
            case "Y":
                return Result.DRAW
            case "Z":
                return Result.WIN


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def find_move(opponent: Self, result: Result) -> Self:
        if result == Result.DRAW: return opponent
        # TODO: Refactor
        match (opponent, result):
            case (Move.ROCK, Result.LOSS):
                return Move.SCISSORS
            case (Move.ROCK, Result.WIN):
                return Move.PAPER
            case (Move.PAPER, Result.LOSS):
                return Move.ROCK
            case (Move.PAPER, Result.WIN):
                return Move.SCISSORS
            case (Move.SCISSORS, Result.LOSS):
                return Move.PAPER
            case (Move.SCISSORS, Result.WIN):
                return Move.ROCK

    @staticmethod
    def fight(opponent: Self, own: Self) -> int:
        value = own.value
        if own == opponent:
            return value + 3

        match (opponent, own):
            case (Move.ROCK, Move.PAPER) | \
                 (Move.PAPER, Move.SCISSORS) | \
                 (Move.SCISSORS, Move.ROCK):
                value += 6
        return value

    @staticmethod
    def from_string(s: str) -> Self:
        match s:
            case "A" | "X":
                return Move.ROCK
            case "B" | "Y":
                return Move.PAPER
            case "C" | "Z":
                return Move.SCISSORS
            case _:
                raise ValueError("Not a valid move")


def convert_pair(pair: List[str]) -> Tuple[Move, Move]:
    assert len(pair) == 2
    l = list(map(lambda x: Move.from_string(x), pair))
    return l[0], l[1]


with open("inputs/day02.txt") as file:
    lines = file.readlines()

    lines = [line.strip().split(" ") for line in lines]
    points = [Move.fight(*convert_pair(line)) for line in lines]
    print(f"Points following strategy: {sum(points)}")

    sum = 0
    for line in lines:
        enemy_move = Move.from_string(line[0])
        result = Result.from_string(line[1])
        own_move = Move.find_move(enemy_move, result)
        sum += Move.fight(enemy_move, own_move)
    print(f"Task 2, points from following strategy: {sum}")

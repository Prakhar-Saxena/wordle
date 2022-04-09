import sys
from enum import Enum
import random

class State(Enum):
    NotIn = 0
    Unknown = 1
    In = 2
    InPosition = 3


class Letter:
    def __init__(self, val: str, position: int, state: State = State.Unknown):
        self.val = val
        self.postion = position
        self.state = state


class Wordle:
    def __init__(self):
        words_file = open("5_letter_words", "r")
        words = words_file.readlines()
        self.word = random.choice(words)

    def __init__(self, word):
        self.word = word

    def is_letter_in_word(self, letter: Letter) -> bool:
        return letter.val in self.word

    def is_the_word(self, input_word) -> bool:
        return input_word == self.word

    def get_Letter(self, letter: Letter) -> list(Letter):
        output = []
        for i in range(self.word):
            c = self.word[i]
            if (letter.val == c):
                if (letter.postion == i):
                    output.append(Letter(c, i, State.InPosition))
                else:
                    output.append(Letter(c, i, State.In))
        return output



def main() -> int:
    words_file = open("5_letter_words", "r")
    words = words_file.readlines()
    print(words[1])


if __name__ == '__main__':
    main()
    sys.exit(0)

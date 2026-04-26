# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


# starting word game
class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        vowels = ["a", "e", "i", "o", "u"]
        p1_vowels = 0
        p2_vowels = 0

        # Player one vowels
        for char in player1_word:
            if char in vowels:
                p1_vowels += 1
        # Player two vowels
        for char in player2_word:
            if char in vowels:
                p2_vowels += 1

        # winner
        if p1_vowels > p2_vowels:
            return 1
        elif p2_vowels > p1_vowels:
            return 2
        else:
            return 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # both not rock paper or scissors
        words = ["rock", "paper", "scissors"]
        # checks
        valid_1 = player1_word in words
        valid_2 = player2_word in words

        if not valid_1 and not valid_2:
            return 0
        elif not valid_2:
            return 1
        elif not valid_1:
            return 2

        # if both words are same
        if player2_word == player1_word:
            return 0

        wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        if wins[player1_word] == player2_word:
            return 1

        elif wins[player2_word] == player1_word:
            return 2

        else:
            return 0

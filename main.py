import random
from datetime import datetime
import os


class HangMan:

    def __init__(self):
        self.word = {}
        self.words = []
        self.gaps = []
        self.placeholder = ''
        self.tries = 0
        self.time = datetime.now()

    def start(self):
        with open("words.txt", "r") as t:
            for i in t.readlines():
                self.words.append(i.replace("\n", ""))
        choice = random.choice(self.words)
        for i_run, value in enumerate(choice):
            self.word[i_run] = value
        st = '_' * len(self.word)
        self.gaps = list(st)
        print(f"Your word is: {st}")
        HangMan.guess(self)

    def guess(self):
        while "_" in self.gaps:
            guess = input("Guess: ").lower()
            self.tries += 1
            if guess in self.placeholder:
                print("You already guessed that!\n")
            elif guess in self.word.values():
                print("Correct!\n")
                for key, val in self.word.items():
                    if guess == val.lower():
                        self.gaps[key] = self.word[[k for k, v in self.word.items() if v == val][0]]
            self.placeholder = ""
            for i in self.gaps:
                self.placeholder += i
            print(self.placeholder)
        self.time = datetime.now() - self.time
        HangMan.score(self)



    def score(self):
        print(f"""
Word: {self.placeholder.title()}
Tries: {self.tries}
Time Taken: {self.time}
        """)


HangMan().start()

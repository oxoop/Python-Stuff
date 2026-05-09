import random


class rps:
    def __init__(self, debug: bool) -> None:
        self.choices = ["r", "p", "s"]
        self.ai = ""
        self.playerop = ""
        if debug == True:
            self.debug = True
        else:
            self.debug = False
        self.winrule = {"r": "s", "p": "r", "s": "p"}
    def getrandom(self, bias):
        
        self.ai = random.choices(self.choices, weights=bias, k=1)[0]
        if self.debug == True:
            print(f"The output is: {self.ai} The type: {type(self.ai)}" )

    def GetUserInput(self):
        playerop = input("""
-------
|R,P,S|
|-> """)
        self.playerop = playerop.lower()
        if self.debug:
            print(f"The player Choose: {self.playerop}, The Type is: {type(self.playerop)}")
    def CheckForRps(self):

        if self.ai == self.playerop:
            print("You tied")
        elif self.winrule[self.playerop] == self.ai:
            print("You win!")
        else:
            print("|You lose")
        print(f"|They choose {self.ai}")
        print("\n  's = scissors, p = paper, r = rock'")
game = rps(False)
game.getrandom([1,1,1])
game.GetUserInput()
game.CheckForRps()


import random
from rich.console import Console
from rich.text import Text
from rich import print 
console = Console()
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
        playerop = console.input("""
[bold red]-------
[bold red]|R,P,S|
[bold blue]|[bold deep_pink]-> """)
        print("[bold blue]|-----|")
        self.playerop = playerop.lower()
        if self.debug:
            print(f"The player Choose: {self.playerop}, The Type is: {type(self.playerop)}")
    def CheckForRps(self):

        if self.ai == self.playerop:
            print("[bold white]|You tied")
        elif self.winrule[self.playerop] == self.ai:
            print("[bold blue]|[italic green]You win!")
        else:
            print("[bold blue]|[italic red]You lose")
        print(f"[bold blue]|[bold yellow]They choose {self.ai}")
        print("\n  [italic]'s = scissors, p = paper, r = rock'")
        
game = rps(False)
game.getrandom([1,1,1])
game.GetUserInput()
game.CheckForRps()

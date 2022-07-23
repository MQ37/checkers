import game
from game.interface import CLIInterface

interface = CLIInterface()

game = game.Game(interface)

while True:
    game.turn()


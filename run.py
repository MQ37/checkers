import game
from game.interface import CLIInterface

interface = CLIInterface()
interface.ask_nicknames()

game = game.Game(interface)

while True:
    game.turn()


from ConsoleInput import *
from Player import *

def testPlayer(*args):
    print player.name

player = Player("Mouse")
console = ConsoleInput(">")
console.addCommand("test",testPlayer)
console.input()
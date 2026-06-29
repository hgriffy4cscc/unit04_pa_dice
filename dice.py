import random

class Dice():
    """simple class to represent a die of varying sides"""
    def __init__(self) -> None:
        self.sides: int = 6
    
    def roll_die(self):
        return random.randint(1,self.sides)

def main():
    """function to control die rolling"""
    die: Dice = Dice(6)
    print (roll_die())

main()

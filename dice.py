import random

class Dice():
    """simple class to represent a die of varying sides"""
    def __init__(self) -> None:
        self.sides: int = 6

    def set_sides(self,sides):
        self.sides = sides

    def roll_die(self):
        return random.randint(1,self.sides)

def main():
    """function to control die rolling"""
    die: Dice = Dice()
    print (die.roll_die())

for i in range(3):
    main()

import random

class Dice():
    """simple class to represent a die of varying sides"""
    def __init__(self) -> None:
        self.sides: int = 6

    def set_sides(self,sides):
        self.sides = sides

    def roll_die(self):
        return random.randint(1,self.sides)
    
    def __repr__(self):
        return f"{self.sides}-sided die"

def main(die_size):
    """function to control die rolling"""
    die_die_size: Dice = Dice()
    die_die_size.set_sides(die_size)
    print(f"10 rolls of a {die_die_size}")
    for i in range(10):
        print (die_die_size.roll_die())

die_sizes: list[int] = [6, 10, 20]

for die_size in die_sizes:
    main(die_size)

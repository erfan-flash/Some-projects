import random
import sys

def main():
    while True:
        roll = input("Choose the number of dices for rolling: ")
        if roll :=check(roll):
            #print(", ".join(map(str, dice(roll))))
            print(*dice(roll) , sep=", ")
        
def check(what):
    while True:
        if what == "exit":
            sys.exit("Bye")
        try:
            if int(what) <2:
                raise ValueError
            return int(what)
        except ValueError:
            print("Invalid Input")
            return False



def dice(n: int=2 ) -> list:
    rolls =[]
    sum =0
    for i in range(n):
        rolls.append(random.randint(1,6))
        sum += rolls[i]
    rolls.append(f"sum ={sum}")
    return rolls

if __name__ =="__main__":
    main()

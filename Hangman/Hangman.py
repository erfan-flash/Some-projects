import random

def main():
    name = input("What is your name? ")
    print(f"Welcome to Hangman, {name}")
    words = ["secret","pancake", "glasses","rojo"]
    word = random.choice(words)
    counter = 3
    guess = [*("_" * len(word))]
    print("WORD: " , *guess)
    while (counter !=0) and ("_" in guess) :
        answer = input("Guess one letter: ")
        if check(answer , word) :
            if letter := validate(answer , guess , word) :
                print(f"Nice try: " , *letter , sep="")
            else:
                counter -=1
                print(f"Wrong answer, You have {counter} tries left.")
        else:
            counter -=1
            print(f"Invalid input, You have {counter} tries.")
    if "_" in guess:
        print("You Lost")
    else:
        print("Congrats,You won")
        
    
def check(answer , word):
    if (len(answer) !=1) and (len(answer) !=len(word)):
        return False
    elif not answer.isalpha():
        return False
    return True

def validate(answer , guess , word):
    if answer not in word:
        return False
    elif len(answer) == len(word):
        answer = [*answer]
        for i in range(len(word)):
            if word[i] == answer[i]:
                guess[i] = answer[i]
    else:
        for i in range(len(word)):
            if word[i] == answer:
                if guess[i] == answer:
                    return False
                guess[i] = answer
    return guess 

    

if __name__ =="__main__":
    main()
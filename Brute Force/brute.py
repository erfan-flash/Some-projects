import itertools
import time
import string

def common_word(word:str) -> str|None:
    with open("common.txt" , "r") as file:
        lines: list[str] = file.read().splitlines()
    for i,common in enumerate(lines, start=1):
        if word == common :
            return f"Common word: {word} (#{i})"

def brute_force(word:str, word_length:int, symbols:bool = False , digits:bool = False) -> str|None:
    selection_list:list[str] = string.ascii_letters
    if digits:
        selection_list += string.digits
    if symbols :
        selection_list += string.punctuation
    counter = 0 
    for guess in itertools.product(selection_list, repeat=word_length):
        counter +=1
        guess ="".join(guess)
        if guess == word:
            return f"{guess} (#{counter})"

def main():
    password = "erfan"
    start_time= time.perf_counter()
    if common := common_word(password):
        print(common)
    else:
        if guess :=brute_force(password , word_length=len(password) , symbols=False , digits = False):
            print(guess)
        else:
            print("intersting word")
    end_time = time.perf_counter()
    print(round(end_time - start_time , ndigits=3) , "s")
        

if __name__ =="__main__":
    main()
        


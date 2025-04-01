def check(password):
    with open("cpc.txt" , "r") as file:
        lines = file.read().splitlines()
        for i, pack in enumerate(lines , start=1):
            if password == pack :
                return f"Your pass is lit! {pack} is number {i} on the list"
        else:
            return f"Your passowrd: {password} is unique"

def main():
    while True:
        password = input("Insert your pass bruh: ")
        if len(password) < 6:
            continue
        print(check(password)) 
        break

if __name__ =="__main__":
    main()
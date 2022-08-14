import random

def guess():
    while True:
        num = input("Guess: ").strip()
        if not num.isdigit():
            print("This is not a valid answer.")
        else:
            num = int(num)
            if num not in range(100):
                print("This is not a valid answer.")
                continue
            else:
                break
    
    return(num)

def hint1(randint):
    if randint % 2 == 0:
        print("Hint No1: The random number is even.")
    else:
        print("Hint No1: The random number is odd.")

def hint2(randint):
    randstr = str(randint)
    digit1 = randstr[1]

    if digit1 != '':
        digit0 = int(randstr[0])
        print(f"Hint No2: The random number is between {(digit0 - 1)*10} and {(digit0 + 1)*10}.")
    else:
        print(f"Hint No2: The random number is between 1 and 10.")

def hint3(randint):
    randstr = str(randint)
    digit1 = randstr[1]

    if digit1 != '':
        digit1 = int(randstr[1])
        print(f"Hint No3: The random number's last digit is {digit1}.")
    else:
        print(f"Hint No3: The random number is between {randint - 3} and {randint + 3}")

def play_again():
    ag = True

    while True:
        play = input("Do you want to play ag?(y/n) ").strip()
        
        if play != 'y' and play != 'n':
            print("This is not a valid answer.")
            continue
        else:
            if play == 'y':
                ag = True
                break
            elif play == 'n':
                ag = False
                break
    
    return(ag)

def main():
    again = True

    while again:
        
        randnum = random.randint(1, 100)
        
        numguess = guess()
        if numguess == randnum:
            print("You guessed the number correctly on the 1st try.Congrats!")
            break
        else:
            hint1(randnum)

        numguess = guess()
        if numguess == randnum:
            print(f"Congrats.The number truly was {randnum}.")
            break
        else:
            hint2(randnum)

        numguess = guess()
        if numguess == randnum:
            print("You got it finally.")
            break
        else:
            hint3(randnum)
        
        numguess = guess()
        if numguess == randnum:
            print(f"At least you got it on the 3rd try.")
            break
        else:
            print(f"Really? You couldn't guess it after all these hints?. The random number is {randnum}")
            break

main()
    




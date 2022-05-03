import re

def text_or_file():
    while True:
        torf = input("Do you want to process a text or import a file?(text/file)\n").strip()
        if torf != 'text' and torf != 'file':
            print("This is not a valid answer")
            continue
        else:
            break
    return(torf)

def open_file():
    while True:
        file_name = input("File name: ").strip()
        try:
            fhand = open(file_name)
            file = fhand.read()
            break
        except:
            print("This file could not be found.")
            continue
    return(file)

def word_or_number():
    while True:
        wn = input("Do you want to find a word or a number?(word/number)\n").strip()
        if wn == 'word' or wn == 'number':
            break
        else:
            print("This is not a valid answer.")
            continue
    return(wn)

def user_word():
    while True:
        word = input("Which word do you want to count?\n").strip()
        if len(re.findall(r"[\w]+",word)) != 1:
            print("This is not a valid answer.")
            continue
        elif not word.isalpha():
            print("This is not a valid answer.")
            continue
        else:
            break
    return(word)

def user_number():
    while True:
        number = input("Which number do you want to count?\n").strip()
        if '-' in number:
            num = number.replace('-','')
            if not num.isdigit():
                print("This is not a valid answer.")
                continue
            else:
                break
        elif not number.isdigit():
            print("This is not a valid answer.")
            continue
        else:
            break
    return(number)

def count_smth_else():
    while True:
        cont = input("Do you want to count something else?(y/n)\n").strip()
        if cont != 'y' and cont != 'n':
            print("This is not a valid answer.")
            continue
        else:
            break
    return(cont)

def times(type:str, value:str , frequency: int):
    if frequency == None:
        print(f"The {type} {value} is not in the text.")
    elif frequency == 1:
        print(f"The {type} {value} is 1 time in the text.")
    else:
        print(f"The {type} {value} is {frequency} times in the text.")

def new_text():
    while True:
        nt = input("Do you want to process another file?(y/n)\n").strip()
        if nt != 'y' and nt != 'n':
            print("This is not a valid answer.")
            continue
        else:
            break
    return(nt)

def word_counter(list: list):
    word_count = {w: list.count(w) for w in list}
    return(word_count)
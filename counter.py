import re
import functions as fc

while True:
    t_or_f = fc.text_or_file()
    if t_or_f == 'file':
        while True:
            rfile = fc.open_file()
            list_ = re.findall(r"[\w]+",rfile.lower())
            if list_ == []:
                print("This is not a valid answer.")
                continue
            else:
                break
        num_list = [num for num in list_ if num.isdigit()]
        word_list = [word for word in list_ if word not in num_list]
        word_count = fc.word_counter(word_list)
        num_count = fc.word_counter(num_list)
        if num_list != []:
            while True:
                word_number = fc.word_or_number()
                if word_number == 'word':
                    word = fc.user_word()
                    word_lower = word.lower()
                    word_freq = word_count.get(word_lower)
                    fc.times('word', word, word_freq)
                    cse = fc.count_smth_else()
                    if cse == 'n':
                        break
                    else:
                        continue
                else:
                    number = fc.user_number()
                    num_freq = num_count.get(number)
                    fc.times('number', number, num_freq)
                    cse = fc.count_smth_else()
                    if cse == 'n':
                        break
                    else:
                        continue
            nt = fc.new_text()
            if nt == 'y':
                continue
            else:
                break
    elif t_or_f == 'text':
        while True:
            text = input("Text: ").strip()
            list_ = re.findall(r"[\w]+",text.lower())
            if list_ == []:
                print("This is not a valid answer.")
                continue
            else:
                break
        num_list = [num for num in list_ if num.isdigit()]
        word_list = [word for word in list_ if word not in num_list]
        word_count = fc.word_counter(word_list)
        num_count = fc.word_counter(num_list)
        if num_list != []:
            while True:
                word_number = fc.word_or_number()
                if word_number == 'word':
                    word = fc.user_word()
                    word_lower = word.lower()
                    word_freq = word_count.get(word_lower)
                    fc.times('word', word, word_freq)
                    cse = fc.count_smth_else()
                    if cse == 'n':
                        break
                    else:
                        continue
                else:
                    number = fc.user_number()
                    num_freq = num_count.get(number)
                    fc.times('number', number, num_freq)
                    cse = fc.count_smth_else()
                    if cse == 'n':
                        break
                    else:
                        continue
            nt = fc.new_text()
            if nt == 'y':
                continue
            else:
                break

print("Shutting down...")
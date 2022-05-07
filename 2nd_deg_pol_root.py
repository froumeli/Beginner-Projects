import functions as fc

while True: 
    coef_list = list()
    for i in range(0, 3):
        while True:
            coef = input(f"Coefficient of term number {i+1}: ").strip()
            try:
                coef = int(coef)
                break
            except:
                print("This is not a valid answer.")
                continue
        coef_list.append(coef)
    a = coef_list[0]
    b = coef_list[1]
    c = coef_list[2]
    if a == 0:
        if b == 0:
            print("This is not a polynomial.")
            continue
        else:
            if c == 0:
                print(f"The polynomial is {b}*x and its root is x = 0.")
                othpol = fc.other_pol()
                if othpol == 'y':
                    continue
                else:
                    break
            else:
                print(f"The polynomial is {b}*x + {c} and its root is {(-c)/b}.")
                othpol = fc.other_pol()
                if othpol == 'y':
                    continue
                else:
                    break
    else:
        print            
    Δ = b^2 - 4*a*c
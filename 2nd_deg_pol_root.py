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
            print(f"This is the constant polynomial {c}.")
            othpol = fc.other_pol()
            if othpol == 'y':
                continue
            else:
                break
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
    else :           
        Δ = b**2 - 4*a*c
        print(Δ)
        if Δ < 0 :
            if a < 0:
                print("The polynomial has no real roots and is negative for every x in R.")
                othpol = fc.other_pol()
                if othpol == 'y':
                    continue
                else:
                    break
            elif a > 0 :
                print("The polynomial has no real roots and is positive for every x in R.")
                othpol = fc.other_pol()
                if othpol == 'y':
                    continue
                else:
                    break
        elif Δ == 0:
            print(f"The polynomial has a double root, which is {(-b)/a}.")
            othpol = fc.other_pol()
            if othpol == 'y':
                continue
            else:
                break
        elif Δ > 0:
            x1 = ((-b) + Δ**(1/2)) / (2*a)
            x2 = ((-b) - Δ**(1/2)) / (2*a)
            print(f"The polynomial has two roots which are:\nx1: {x1}\nx2: {x2}")
            othpol = fc.other_pol()
            if othpol == 'y':
                continue
            else:
                break

print("Shutting down...")
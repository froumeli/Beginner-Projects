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
pol = lambda x: a*x^2 + b*x + c
print(f"The polynomial is {a}*x^2 + {b}*x + {c}")

Δ = b^2 - 4*a*c

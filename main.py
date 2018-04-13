
while True:

    try:
        getal1 = float(input("Voer het eerste getal in: "))
        break
    except Exception:
        print("Kies een getal")


while True:

    try:
        getal2 = float(input("Voer het tweede getal in: "))
        break
    except Exception:
        print("Kies een getal")
    
print("1) plus")
print("2) min")
print("3) keer")
print("4) gedeeld door")
print("5) machtverheffen")

while True:

    operator = input("Kies de operator: ")

    if  operator == 1:
        uitkomst = getal1 + getal2

    elif  operator == 2:
        uitkomst = getal1 - getal2

    elif  operator == 3:
        uitkomst = getal1 * getal2

    elif  operator == 4:
        try:
            uitkomst = getal1 / getal2
        except ZeroDivisionError:
            uitkomst = "Delen door nul is flauwekul"

    elif  operator == 5:
        try:
            uitkomst = getal1 ** getal2
        except OverflowError:
            uitkomst = "Te groot getal"
    else:
        print("Kies een getal van 1 t/m 5")

    if operator >= 1 and operator <=5:
        break

print(uitkomst)

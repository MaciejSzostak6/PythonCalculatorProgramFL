import time

def funPrintMenu():
    print("+----------MENU----------+")
    print("|1. Suma                 |")
    print("|2. Różnica              |")
    print("|3. Iloczyn              |")
    print("|4. Iloraz               |")
    print("|5. Modulo               |")
    print("|6. Pierwiastek          |")
    print("+------------------------+")


def funLiczby():
    funPrintMenu()
    wybor = int(input("Podaj numer operacji(1-6): "))

    if wybor!=1 and wybor!=2 and wybor!=3 and wybor!=4 and wybor!=5 and wybor!=6:
        print("Nie ma takiej operacji.")
        time.sleep(1)
        funReturnToMenu()
    
    else:
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))

        if wybor == 1:
            suma = a + b
            print(f"{a} + {b} = {suma}")

        elif wybor == 2:
            roznica = a - b
            print(f"{a} - {b} = {roznica}")

        elif wybor == 3:
            iloczyn = a * b
            print(f"{a} * {b} = {iloczyn}")

        elif wybor == 4:
            iloraz = a / b
            print(f"{a} / {b} = {round(iloraz, 2)}")

        elif wybor == 5:
            modulo = a % b
            print(f"{a} % {b} = {modulo}")

        elif wybor == 6:
            pierwiastek = a ** b
            print(f"{a} ** {b} = {pierwiastek}")

    return "Koniec programu"
def funReturnToMain():
    print()

def funReturnToMenu():
    funLiczby()


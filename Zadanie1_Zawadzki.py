#Stworzenie menu
def srednia_arytmetyczna():
    print("Wybrałeś opcję 1!")

def opcja2():
    print("Wybrałeś opcję 2!")

def opcja3():
    print("Wybrałeś opcję 3!")

def opcja4():
    print("Wybrałeś opcję 4!")

def menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Opcja 1")
        print("2. Opcja 2")
        print("3. Opcja 3")
        print("4. Opcja 4")
        print("0. Zakończ")

        wybor = input("Wybierz numer opcji: ")

        if wybor == '1':
            opcja1()
        elif wybor == '2':
            opcja2()
        elif wybor == '3':
            opcja3()
        elif wybor == '4':
            opcja4()
        elif wybor == '0':
            print("Zakończenie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

# Uruchomienie menu
menu()
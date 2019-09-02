from stos import Stos
from kolejka import Fifo_dowiazane
from kolejka import Node
from sterta import Sterta
import os

def run():
    print ("Wybierz strukture danych: ")
    st = Sterta()
    choice = int(input("(1) - Stos \n(2) - Kolejka\n>> "))
    if (choice == 1):
        os.system('cls')  
        s = Stos()
        while(True):
            print ("Elementy sterty: ")
            print (st.all_ele())
            print ("Wybierz operacje: ")
            choice_stos = int(input("(1) - push\n(2) - pop\n(3) - top\n(4) - is empty\n>> "))
            if (choice_stos == 1):
                os.system('cls') 
                data_stos = input("Dodaj dana do stosu: \n>> ")
                if (st.find_ele(data_stos) == True):
                    print ("Element jest na stercie")
                if (st.find_ele(data_stos) == False):
                    st.add_ele(data_stos)
                    print ("Dodano do sterty")
                s.push(data_stos)
                print ("Dodano do stosu i usunieto ze sterty")
                st.rem_ele(data_stos)
                input(">> [enter]")
                os.system('cls')
                print("Aktualny stos: ")
                for i in s.tablica():
                    print ("--------------")
                    print (i)
                    print ("--------------")
            if (choice_stos == 2):
                os.system('cls')
                if (s.is_empty() == True):
                    print ("Stos jest pusty!")
                else:
                    print("Element zabrany ze stosu: ")
                    res = s.pop()
                    print(res)
                    st.add_ele(res)
                    print("Dodano do sterty")
                    print("Aktualny stos: ")
                    for i in s.tablica():
                        print ("--------------")
                        print (i)
                        print ("--------------")
            if (choice_stos == 3):
                os.system('cls')
                if (s.top() == False):
                    print ("Stos jest pusty!")
                else:
                    print (s.top())
            if (choice_stos == 4):
                os.system('cls')
                if (s.is_empty() == True):
                    print ("Stos jest pusty!")
                else:
                    print ("Stos nie jest pusty!")
    if (choice == 2):
        os.system('cls') 
        f = Fifo_dowiazane()
        kolejka = []
        while(True):
            print ("Elementy sterty: ")
            print (st.all_ele())
            print ("Wybierz operacje: ")
            choice_kolejka = int(input("(1) - enqueue\n(2) - dequeue\n(3) - is empty\n(4) - first\n>> "))
            if (choice_kolejka == 1):
                os.system('cls') 
                data_kolejka = input("Dodaj dana do kolejki: \n>> ")
                f.enqueue(data_kolejka)
                kolejka.append(data_kolejka)
                if (st.find_ele(data_kolejka) == True):
                    print ("Element jest na stercie")
                if (st.find_ele(data_kolejka) == False):
                    st.add_ele(data_kolejka)
                    print ("Dodano do sterty")
                print ("Dodano do kolejki i usunieto ze sterty")
                st.rem_ele(data_kolejka)
                input(">> [enter] ")
                os.system('cls')
                print("Aktualna kolejka: ")
                for i in kolejka:
                    print ("--------------")
                    print (i)
                    print ("--------------")
            if (choice_kolejka == 2):
                os.system('cls')
                if (f.is_empty() == True):
                    print ("Kolejka jest pusta!")
                else:
                    print("Element zabrany z kolejki: ")
                    res = f.first()
                    print(res)
                    del kolejka[0]
                    f.dequeue()
                    st.add_ele(res)
                    print("Dodano do sterty")
                    print("Aktualna kolejka: ")
                    for i in kolejka:
                        print ("--------------")
                        print (i)
                        print ("--------------")
            if (choice_kolejka == 3):
                os.system('cls')
                if (f.is_empty() == True):
                    print ("Kolejka jest pusta!")
                else:
                    print ("Kolejka nie jest pusta!")
            if (choice_kolejka == 4):
                os.system('cls')
                if (f.first() == False):
                    print ("Kolejka jest pusta!")
                else:
                    print (f.first())

run()




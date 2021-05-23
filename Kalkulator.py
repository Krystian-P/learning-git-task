import logging

def kalkulator(działanie, pierwsza_liczba, druga_liczba):

    if działanie==1:
        logging.info(f"Dodaję {pierwsza_liczba} oraz {druga_liczba}")
        wynik=pierwsza_liczba+druga_liczba

    elif działanie==2:
        logging.info(f"Odejmuję {pierwsza_liczba} oraz {druga_liczba}")
        wynik= pierwsza_liczba-druga_liczba

    elif działanie==3:
        logging.info(f"Mnożę {pierwsza_liczba} oraz {druga_liczba}")
        wynik= pierwsza_liczba*druga_liczba

    elif działanie==4:
        logging.info(f"Dzielę {pierwsza_liczba} oraz {druga_liczba}")
        wynik= pierwsza_liczba/druga_liczba

    else:
        logging.WARN("nie ma takiej opcji")
    print(f"Twój wynik wynosi: {wynik}")

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    calk=int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawania, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:  "))
    first_number=int(input("Podaj pierwszy składnik:"))
    second_number=int(input("Podaj drugi składnik:"))
kalkulator(calk,first_number,second_number)
class Card:
    def __init__(self, name, surname, company, number):
        self.name = name
        self.surname = surname
        self.company = company
        self.number = number
Person_1 = Card("Kate", "Grayer", "ABCO Food", "978-606-8889")
Person_2 = Card("Mateusz", "Czarnecki", "Envirotecture Design Service", "79 572 58 45")
Person_3 = Card("Seweryna", "Wysocka", "Hanover Shoe", "79 444 93 49")
Person_4 = Card("Michał", "Wojciechowski", "Williams Bros.", "69 931 51 67")
Person_5 = Card("Jaromir", "Tomaszewski", "Saturday Matinee","78 849 35 27")

Card_Book=[Person_1, Person_2, Person_3, Person_4, Person_5]

for Person in Card_Book:
    print(Person.name, Person.surname, Person.number)
class Mieszkanie:
    def __init__(self, Miasto, Cena, Metraz, Pietro, Typ):
        self.Miasto = Miasto
        self.Metraz = str(Metraz)
        self.Pietro = str(Pietro)
        self.Cena = str(Cena)
        self.Typ = Typ

    def __str__(self):
        return 'Mieszkanie = ( Miasto : ' + self.Miasto + ', Cena : ' + self.Cena + ', Metraż : ' + \
            self.Metraz + ', Numer piętra : ' + self.Pietro + ', Typ : ' + self.Typ + ').'


mieszkanie_1 = Mieszkanie('Kraków', 550567.567, 65.5, 5, 'Mieszkanie w bloku')
mieszkanie_2 = Mieszkanie('Kraków', 700733.43, 93.4, 7, 'Mieszkanie w bloku')
mieszkanie_3 = Mieszkanie(
    'Warszawa',
    1200909.99,
    110.1,
    6,
    'Mieszkanie w bloku')
mieszkanie_2 = Mieszkanie('Poznań', 350551.67, 31.7, 3, 'Mieszkanie w bloku')
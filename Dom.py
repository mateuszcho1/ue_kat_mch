class Dom:
    def __init__(self, Miejscowosc, Cena, Metraz, Pietra, Typ):
        self.Miejscowosc = Miejscowosc
        self.Cena = str(Cena)
        self.Metraz = str(Metraz)
        self.Pietra = str(Pietra)
        self.Typ = Typ

    def __str__(self):
        return 'Dom = ( Miejscowość : ' + self.Miejscowosc + ', Cena : ' + self.Cena + ', Metraż : ' + \
            self.Metraz + ', Ilość kondygnacji : ' + self.Pietra + ', Typ : ' + self.Typ + ').'


Dom_1 = Dom('Słomniki', 400000, 120.5, 2, 'Dom wolnostojący')
Dom_2 = Dom('Kielce', 500125.55, 199.87, 3, 'Dom wolnostojący')
Dom_3 = Dom('Dąbrowa Górnicza', 600125.501, 185.55, 2, 'Bliźniak')
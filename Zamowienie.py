from Developer import Developer_1, Developer_2
from Dom import Dom_1, Dom_2, Dom_3
from Mieszkanie import mieszkanie_1, mieszkanie_2, mieszkanie_3


class Zamowienie:
    def __init__(self, Developer, Typ_posiadlosci, Cena, Metraz):
        self.Developer = Developer
        self.Typ_posiadlosci = Typ_posiadlosci
        self.Cena = Cena
        self.Metraz = Metraz

    def __str__(self):
        return 'Zamówienie : Developer : ' + self.Developer + ', Typ : ' + self.Typ_posiadlosci + \
            ', Łączna cena : ' + self.Cena + ', Łączny metraż : ' + self.Metraz + ').'


Zamowienie_1 = Zamowienie(
    Developer_1.Nazwa,
    Dom_3.Typ + ' i ' + mieszkanie_1.Typ,
    str(float(round(float(Dom_3.Cena) + float(mieszkanie_1.Cena), 2))),
    str(float(Dom_3.Metraz) + float(mieszkanie_1.Metraz)))
print(Zamowienie_1)
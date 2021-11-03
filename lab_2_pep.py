# Zadanie 2. a.
def names(name1, name2, name3, name4, name5):
    print(f'Cześć {name1}, {name2}, {name3}, {name4}, {name5}')


names('Mateusz', 'Anna', 'Jarosław', 'Bartosz', 'Zuzanna')

###############################################

# Zadanie 2. b. i.

lista_1 = []
lista_2 = []
n = int(input("\n Wprowdz ilość liczb"))
print("\n Wproadz elementy")
for i in range(n):
    lista_1.append(int(input()))
x = int(input("\n Wproadz liczbę do mnożenia"))
for i in lista_1:
    lista_2.append(x * i)
print(lista_2)

###############################################

# Zadanie 2. b. ii.


def liczby_b(liczba1, liczba2, liczba3, liczba4, liczba5):
    list_numbers = [
        liczba1 * 2,
        liczba2 * 2,
        liczba3 * 2,
        liczba4 * 2,
        liczba5 * 2]
    print(list_numbers)


liczby_b(1, 2, 3, 4, 5)

###############################################

# Zadanie 2. c.

moja_lista = list(range(10))
for i in moja_lista:
    if i % 2 == 0:
        print(i, end=" ")

###############################################

# Zadanie 2. d.

moja_lista = list(range(10))
for x in moja_lista[::2]:
    print(x)

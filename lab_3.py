# Zadanie 1.

# def function_string(name, surname):
#     print("Cześć " + name + " " + surname)
# function_string("Mateusz", "Chojnacki")

# Zadanie 2.

# def MultiplyNumbers(number_1,number_2):
#     print(number_1*number_2)
# MultiplyNumbers(2,3)

# Zadanie 3.

# def CheckEvenNumber(x):
#     print(x % 2 == 0)
#     if x % 2 == 0:
#         print("Liczba parzysta !")
#     else:
#         print("Liczba nieparzysta !")
# CheckEvenNumber(4)

# Zadanie 4.

# def CheckThreeNumbers(x,y,z):
#     print(x+y >= z)
# CheckThreeNumbers(1,2,4)

# Zadanie 5.

# list = [1,2,3,4,5]
# def CheckListToInt(lista,n):
#     if n in lista:
#         print("Element jest w liście")
#     else:
#         print("Takiego elementu nie ma w liście !")
# CheckListToInt(list,6)

# Zadanie 6.

# list_1 = [1,2,4,5]
# list_2 = [2,3,5,6,7]

# print("Lista 1")
# print(list_1)
# print("Lista 2")
# print(list_2)

# def UnionList(First_list,Second_list):
#     list_3 = First_list + Second_list
#     print("Lista złączona: ")
#     print(list_3)
#     non_duplicate_list = list(dict.fromkeys(list_3))
#     print("Lista bez duplikatów :")
#     print(non_duplicate_list)
#     final = [] 
#     for n in non_duplicate_list:
#         final.append(n**3)
#     print("Ostateczna lista !")
#     print(final)
# UnionList(list_1,list_2)

# Zadanie 7. W trakcie ...

# import json
# import requests
# response = requests.get("https://api.openbrewerydb.org/breweries/search?query=do")
# # print(response)
# r = response.json()
# data = json.loads(r)
# for n in data:
#     print(n)

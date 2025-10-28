"""
Scrie un program în Python care declara un sir cu continutul copiat de pe internet, 
dintr-un articol de stiri in limba romana și efectuează pe acel articol(care este stocat ca un sir de caractere) următoarele operații:

Împarte șirul în două părți egale.
Pe prima parte:
-Transformă toate literele în majuscule.
-Elimină toate spațiile goale de la începutul și finalul șirului.
Pe a doua parte:
-Inversează ordinea caracterelor.
-Transformă prima literă în majusculă.
-Elimină toate caracterele de punctuație (., ,, !, ?) din această parte.
Combină cele două părți și afișează rezultatul.

"""

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

middle = len(text) // 2

first_half = text[:middle]
second_half = text[middle:]

first_half = first_half.upper().strip()

second_half = ''.join(reversed(second_half))
second_half = second_half.capitalize()
second_half = ''.join(char for char in second_half if char not in '.!?,')

result = first_half + second_half

print(result)
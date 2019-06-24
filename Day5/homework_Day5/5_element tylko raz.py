# program znajdujacy wartosci, ktre wystepuja tylko raz

from collections import Counter

lista_a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
list = Counter(lista_a)

appears_once = []

for element in list:
    if list[element] <= 1:
        appears_once.append(element)

print(lista_a)
print('Wartosci wystepujace tylko raz w liscie powyzej to', appears_once)


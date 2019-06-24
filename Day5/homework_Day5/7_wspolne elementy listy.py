# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True


lista_1 = [2, 45, 678, 54, 5, 6, 7, 10]
lista_2 = [2, 67, 890, 8, 22, 1, 2, 11, 51]

print(lista_1, lista_2)

# a = int(input('Podaj element wystepujacy w obu listach: '))
for element in lista_1:
    if element in lista_2:
        print('True')
        break
else:
    print('Listy nie maja wspolnego elementu')


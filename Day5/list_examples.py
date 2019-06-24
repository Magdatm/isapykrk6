# uzytkownik podaje dwie liczby poczatek i koniec

start = int(input('Podaj liczbe poczatkowa: '))
stop = int(input('Podaj liczbe koncowa: '))

my_list = list(range(start, stop))

#index = int(input('Podaj index: '))

#print(my_list[index])

to_find = int(input('Podaj wartosc szukana: '))
found = False

for element in my_list:
    if element == to_find:
        print('Znaleziono wartosc szukana', to_find)
        found = True
        break

    #if not found:
       # print('Nie znaleziono wartosci szukanej')

else:
    print('Nie znaleziono')



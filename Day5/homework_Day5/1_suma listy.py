# napisz program sumujący wszystkie elementy w liscie

start = int(input('Podaj liczbe poczatkowa: '))
stop = int(input('Podaj liczbe koncowa: '))

my_list = list(range(start, stop))

print(my_list)

suma = sum(my_list)

print('Suma elementow w Twojej liscie to: ' , suma)
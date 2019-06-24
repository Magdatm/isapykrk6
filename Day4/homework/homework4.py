number = input('Podaj liczbe dla ktorej chcesz zobaczyc tabliczke mnozenia: ')
number = int(number)

for x in range(11):
    print(number, '*', x, '=', number ^ x)
    continue

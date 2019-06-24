# 1. pobierz od uzytkownika dane i sprawdz czy jest to liczba
# 2. Czy liczba jest podzielna przez 3, 5, 7
# 3. Jezeli nie jest to liczna wyswietl: niepoprawne dane

dane = input('Podaj liczbe: ')
if dane.isdigit()
    liczba = int(dane)

    if liczba % 3==0:
    print ('liczba dzieli sie przez 3')

    if liczba % 5==0:
    print('liczba dzieli sie przez 5')

    if liczba % 7 ==0:
    print('liczba dzieli sie przez 7')

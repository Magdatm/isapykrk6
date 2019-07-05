try:
    #1/0
    raise ValueError("Nie zgadza sie wartosc")
except (ZeroDivisionError, ValueError):
    print('Nie dziel przez zero')
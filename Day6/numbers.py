def suma_dwoch_wartosci(*args):
    # z = x + y
    # print(z)
    total = 0
    for element in args:
        total += element
    print(total)

    print(sum(args))

suma_dwoch_wartosci(2, 3)
suma_dwoch_wartosci(-2, 3)
suma_dwoch_wartosci(1, 2, 3)
suma_dwoch_wartosci(3)
suma_dwoch_wartosci()
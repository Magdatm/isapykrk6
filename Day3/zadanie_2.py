data = input('Podaj wartosc temperatury: ')

value = data[0:-1]
unit = data[-1]

if value.isdigit():
    value_converted = int(value)

    if unit.lower() == 'f' or unit.upper() == 'F':
        temp_stC = (value_converted - 32) * (5/9)
        print('temperatura podana przez Ciebie w st Celcjusza to', temp_stC)

    elif unit.lower() == 'c' or unit.upper() == 'C':
        temp_stF = value_converted * (9/5) + 32
        print('temperatura podana przez Ciebie w stopniach Faranheita to: ', temp_stF)

    else:
        print('podano niewlasciwe dane')

else:
    print('podaj liczbe!')

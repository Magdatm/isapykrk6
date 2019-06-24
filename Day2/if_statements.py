# % operator modulo

user_input = input('Podaj liczbe calkowita: ')
# user_input = int(user_input)

if user_input.isdigit():
    user_input = int(user_input)
    if user_input % 2:                                     # Pythonic Code if user_input % 2 != 0
        print (user_input, 'jest nieparzysta')
    else:
        print (user_input, 'jest parzysta')
else:
    print('podales niepoprawne dane wejsciowe')
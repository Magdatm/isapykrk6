postcode = input('Podaj kod pocztowy')

# if  postcode[:2].isdigit() and postcode[3:].isdigit():
#     print('kod pocztowy jest poprawny')
# else:
#     print('kod pocztowy jest niepoprawny')



postcode_splitted = postcode.split('-')

if postcode_splitted[0].isdigit() and postcode_splitted[1].isdigit()
    print('Kod pocztowy jest poprawny')
else:
    print('Kod pocztowy jest niepoprawny')


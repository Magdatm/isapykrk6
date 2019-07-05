from pprint import pprint


phone_book = {'Kowalski': 'Jan',
              'Nowak': 'Anna',
              'Lalak': 'Przemyslaw'}

# wyluskanie wartosci klucza
last_name = phone_book['Kowalski']
print(last_name)

phone_book['Pythonowy'] = 'Python'      # dodanie nowego klucza do slownika
phone_book['Pythonowy'] = None    # zarezerwowanie nazwy w slowniku

# iterowanie po slowniku (tylko klucze!)
for element in phone_book:
    print(element)


# iterowanie po slowniku (tylko wartosc!)
for key in phone_book:
    print(phone_book[key])


# iterowanie po slowniku (klucze i wartoci)
for key, value in phone_book.items():
    print(key, value)


print(type(phone_book.items()))



print(phone_book)
phone_book['Lalak'] = 'Przemyslaw Adam'
print(phone_book)

phone_book_copy = phone_book.copy()
phone_book['Wick'] = 'John'

phone_book.update(phone_book_copy)
print(phone_book)


phone_book.update(Balboa='Rocky')
pprint(phone_book)


# usuwanie klucza ze slownika
popped_value = phone_book.pop('Lalak')
print(popped_value)


#usuwanie klucza ze slownika
del phone_book['Nowak']



#phone_book['Creed']                #   ERROR!

# wyciaganie wartosci ze slownika
print(phone_book.get('Wick'))
print(phone_book.get('Creed', 'Unknown'))


#tworzymy pusty slownik
some_dict = {}   #dict()


# dict comprehension
some_dict = {x: x**2 for x in range(10)}
print(some_dict)


# for key in some_dict:
#     if key %2:
#         del some_dict[key]
# pprint(some_dict)                   # niewiadomy wynik, bo iterujac usuwamy element!!   DON'T DO THIS!


def foo(*args, **kwargs):
    print(locals())

foo(1, 2)
foo(1, 5, some='value')
foo(argument=123)


















phone_book = {
    'Kowalski': 'Jan',
    'Nowak': 'Anna',
    'Lalak': 'Przemyslaw'
}


with open('phone_book.txt', 'w') as phone_book_file:
    phone_book_file.writelines(phone_book)


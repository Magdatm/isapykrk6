phone_book = {
    'Kowalski': 'Jan',
    'Nowak': 'Anna',
    'Lalak': 'Przemyslaw'
}

with open('phone_book.txt', 'r') as phone_book_file:
    # text = phone_book_file.read()
    # print(text)
    # text = phone_book_file.read(6)
    # print(text)

    for line in phone_book_file:
        print(line)



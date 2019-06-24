import string

letters_counter = 0
number_counters = 0

text = 'akndowed82398   hdbdoi3hd2)('

for element in text:
    if element in string.ascii_letters:
        letters_counter += 1
    elif element in string.digits:
        number_counters += 1

print(number_counters)
print(letters_counter)
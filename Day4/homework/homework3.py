word = input('Podaj ciag liter i cyfr: ')

letter = 'qwertyuiopasdfghjklzxcvbnm'
number = '0123456789'

counter_letter = 0
counter_number = 0

for x in word:
    if x in letter:
        counter_letter += 1

    elif x in number:
        counter_number += 1

    continue

print('Ilosc liter to: ', counter_letter)
print('Ilosc cyfr to: ', counter_number)




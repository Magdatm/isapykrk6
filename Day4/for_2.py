magic = 'abracadabra'

counter_v = 0
counter_c = 0

vowels = 'a'
consonants = 'brcd'


for char in magic:
    if char in vowels:
        counter_v +=1

print (f'Liczba samoglosek wynosi: {counter_v}')


for char in magic:
    if char in consonants:
        counter_c += 1

print(f'Liczba spolglosek wynosi: {counter_c}')





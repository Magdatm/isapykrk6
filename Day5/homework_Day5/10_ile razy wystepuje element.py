# oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# druga - moze jest jakis modul gotowy???

my_list = [10, 10, 20, 10, 10, 20, 10, 20, 20, 20, 40, 50, 40, 10, 30, 50, 50, 30]

counter_10 = 0
counter_20 = 0
counter_30 = 0
counter_40 = 0
counter_50 = 0

for element in my_list:
    if element == 10:
        counter_10 +=1
    elif element == 20:
        counter_20 += 1
    elif element == 30:
        counter_30 += 1
    elif element == 40:
        counter_40 += 1
    elif element == 50:
        counter_50 += 1

print(' Ilosc wystepowania 10 to: ', counter_10, '\n','Ilosc wystepowania 20 to: ', counter_20, '\n','Ilosc wystepowania 30 to: ',
      counter_30, '\n','Ilosc wystepowania 40 to: ', counter_40, '\n','Ilosc wystepowania 50 to: ', counter_50)


from collections import Counter

list = Counter(my_list)
print(list)
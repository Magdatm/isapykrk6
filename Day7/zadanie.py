# zlicz wystapienia kazdego znaku wystepujacego w tekscie
# jedna linia = jeden znak/slowo

# from pprint import pprint
#
# attempt_number = {}
#
#
# with open('random_words.txt', 'r') as random_words_file:
#     for line in random_words_file:
#         key = line.strip()
#         if key in attempt_number:
#             attempt_number[key] += 1
#         else:
#             attempt_number[key] = 1
#     pprint(attempt_number)



# Drugi sposob bardziej w stylu Python!
from collections import Counter

with open('random_words.txt', 'r') as random_words_file:
    # lines = [line.strip() for line in random_words_file]              # SUPER PYTHON!!!
    lines = []
    for line in random_words_file:
        lines.append(line.strip())
    print(Counter(lines))



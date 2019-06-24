text = "John's house is called \"supernova\""

print(text)


print(text[3])

print(text[-1])

print(text[-4])

text2= 'Ala ma kota'

print(text2)


# my_string[start:end]     end jest zbiorem otwartym wiec nie lapie sie tylko znak przed nim

print(text2[0:3])

print(text2[0:8:2])

print(text2[-5:-1:2])

print(text2[-1:-5:-2])



to_replace = 'kota'
new_value = 'psa'

new_text = text2.replace(to_replace, new_value)

print(new_text)
print(text2)

text2 = text2[:7] + new_value
print(text2)
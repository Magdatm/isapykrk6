text = 'ala ma kota'
text2 = "ala ma kota"

print(text == text2)

print(text.capitalize())

text_upercased = text.upper()
print(text)
print(text_upercased)



length = len(text)
message = 'Dlugosc tekstu to:'
print(message, length)


#todo wyswietl na ekranie tekst:
# todo 'pierwszy znak tekstu to: {znak}'

znak = text [0]
print('pierwszy znak tektu to:', znak)





#todo wyswietl na ekranie tekst:
# todo 'ostatni znak tekstu to: {znak}'

message = 'Ostatni znak tekstu to:'
print(message, text[length-1])
print(message, text[len(text)-2])


 
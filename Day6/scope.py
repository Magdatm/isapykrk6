name = 'jan'

# NAMESPACE
def print_name(name):
    name_capitalised = name.capitalize()
    print(name_capitalised)
    print(locals())
    print(name)


# ERROR
# print(name_capitalised)
print_name('adam')


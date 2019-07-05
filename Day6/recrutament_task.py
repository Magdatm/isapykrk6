# The bed
# def foo(value, words_database=[]):
#     words_database.append(value)
#     print(words_database)

# The good!
def foo(value, my_list = None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list)


foo(1)
foo(2, [3, 4])
foo(5, [])
foo(8, [1])
foo(10)



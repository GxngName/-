def list_to_dict(my_list):
    dictionary = {}
    for i in my_list:
        dictionary[i] = i
    return dictionary

my_list = [Хорошо]
my_dict = list_to_dict(my_list)
print(my_dict)
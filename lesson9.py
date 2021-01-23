d = {'a':1, 'b':2, 'c':3, 4:10, "Hi":"How are you?"}

d1 = dict.fromkeys(['a', 'b', 'c'])

d2 ={i: i**2 for i in range (1, 20, 3)}


#print(list(d.items())[0][1])

#print(list(d.values())[0])

d3 = d1.copy()
d3['a'] = 100

#print(d3.get('d', 200))

#print(d)
#d.update(d3)
#print(d)

#for key, value in d:
#    print(key, value)

def list_to_dict(my_list):
    dictionary = {}
    for i in my_list:
        dictionary[i] = i
    return dictionary

my_list = [4, 7, 2 , 8, 5, 3]
my_dict = list_to_dict(my_list)
#print(my_dict)

my_set = {'Hello', 'World', 100, 'a'}

my_set1 = set('Hello')
print(my_set1)

set1 = {1,2,3}
set2 = {1,2,3,4}
print(set1.issubset)
list1 = [1, "Misha", 7.1]
#list2 = list("Misha")
print(list1[0:10])
 
number_list = [4,5,5,4,6,3]
number_list.append("Weather")
number_list.append(400)
print(number_list)
number_list.insert(0,"WarZone")
print(number_list)
number_list.remove('WarZone')
print(number_list)
number_list.pop(6)
print(number_list)
new_list = number_list[0:2].copy()
print(new_list)


days_list = [4,2,6,5,3,7,9]
days_list.sort()

#letters_list ["z", "x", "X"]
#letters_list.sort()
#print(letters_list)
#print(days_list)

new_numbered_list = []
for i in range (4,15):
    if (i % 2==0 ):
        new_numbered_list.append(i)
print(new_numbered_list)

b = [3*i for i in range(4,15) if i % 2 == 0]
print(b)

for element in b:
    print(element)

b[0] = 100
print(b)

c = (1,2,3,4)
print(c)
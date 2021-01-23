def swap(j, our_list):
    our_list[j], our_list [j+1] = our_list[j+1], our_list[j]


def bubble_sort(my_list):
    N = len(my_list)
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if  my_list[j] > my_list[j+1]:
                swap(j, my_list)

    return my_list 

list1 = [56, 33, 98, 1, 3, 7, 102, 908]
print(bubble_sort(list1))
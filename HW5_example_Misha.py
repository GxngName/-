#Вводим функцию "count_odd_and_even"
def count_odd_and_even():
    #Присваиваем number к int и просим ввести число
    number = int(input("Введите число, для которого мы посчитаем количество чётных и нечетных цифр: "))
    #Четные
    even = 0
    #Нечетные
    odd = 0
    #Начинаем цикл. Пока number больше нуля
    while number > 0:
        #Остаток - number делим с остатком на 10
        rest = number % 10
       #Если остаток делим на 2 равный 0
        if rest % 2 == 0:
           #Прибавляет 1 к even
            even += 1
        else:
            #Прибавляет 1 к odd
            odd +=1
        #Присваиваем number: number делённое на 10 с целочисленным остатком
        number = number // 10
    #Просим функцию вернуть чётные и нечётные числа
    return even, odd

#Эта операция - распаковка, то есть в even и odd
#сейчас запишутся числа, которые возвращает функция

#Присваиваем чётным и нечётным числам имя функции
even, odd = count_odd_and_even()
#Просим напечатать кол-во чётных и нечётных чисел
print(f"Количество чётных цифр в числе: {even}, нечётных: {odd}")

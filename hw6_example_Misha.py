#Мы вводим функцию count_iterations_and_result
def count_iterations_and_result():
   #Цикл - пока выполняется
    while True:
        #"Поппробуй"
        try:
            #Присваиваем number и просим ввести число  не меньше 500
            number = int(input("Введите число не меньше 500: "))
        #Обработка ошибок ValueError (вводится не число)
        except ValueError:
            #Напечатаем "Вы ввели не число"
            print("Вы ввели не число!")
        #Иначе
        else:
            #Если number меньше 500
            if number < 500:
                #Напечатаем "Вы ввели число меньще 500"
                print("Вы ввели число меньще 500")
                #Переходим к следующему пункту
                continue
            #Иначе
            else:
               #Прерывает цикл
                break
   #Переменная
    counter = 0
    #Цикл
    while number > 40:
       #Делим на 2 без остатка
        number /= 2
        #Добавляем к переменной
        counter += 1

    #Возвращяем number, counter
    return number, counter


#Напечатаем count_iterations_and_result
print(count_iterations_and_result())
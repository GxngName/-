try:
    raw = input("Введите число от 0 до 59: ")
    number = int(raw)
    if (0 <= number <= 59) :
        print("Всё верно")
except ValueError:
    try:
        raw = input("Попробуйте ещё раз: ")
        number = int(raw)
        if (0 <= number <= 59) :
            print("Всё верно")
    except ValueError:
        print("Конец")
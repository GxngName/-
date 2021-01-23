def da():
    int(input("Введите число не меньше 500: "))
   while True:
        try:
            age = int(input("Введите число не меньше 500: "))
        except ValueError:
            continue
        else:
            break
    return age





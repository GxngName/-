with open('try.txt', 'r+') as f:
    f_str = f.read()
    f_str = f_str.upper()
    f.write(f_str)

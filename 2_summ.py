def summator():
    sum=0
    while True:        
        a = input('введите число: ')
        if a.isdigit():
            sum += int(a)
            print(sum)
        elif a == "":
            break
        else:
            print("Это не число!")
        
    

summator()

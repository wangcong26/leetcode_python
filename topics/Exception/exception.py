if __name__ == '__main__':
    try:
        f = open('currupt_file.txt')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print('Error!')
    else:
        print(f.read())
        f.close()
    finally:
        print("Executing Finally...")

    list_int = [8, 0, 3, 10, 0]
    for num in list_int:
        try:
            div = 10 / num
        except ZeroDivisionError as e:
            print(num)

    try:
        num_int = int(100)
    except ValueError as e:
        print(e)
        try:
            zero = 10 / 0
        except ZeroDivisionError as e:
            print(e)


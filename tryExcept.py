try:
    num = int(input("enter a number: "))
    print(num)
except ValueError:
    print("invalid input")
except ZeroDivisionError as err:
    print(err)
enter = int(input("Entra com um numero: "))

if enter % 5 == 0:
    print("FizzBuzz")

elif enter % 3 == 0:
    print("FizzBuzz")

elif enter % 3 == 1 and enter % 5 == 1:
    print(enter)

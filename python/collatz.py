# Reduces any entered integer to 1.

def collatz(number):
    if number % 2 == 0:         # even integer
        print(number // 2)
        return number // 2
    elif number % 2 == 1:       # odd integer
        print(3 * number + 1)
        return 3 * number + 1

def apply_collatz():
        try:
            number = int(input("Please enter an integer: "))
        except ValueError or NameError:
            number = int(input("Please enter a valid integer: "))
        result = collatz(number)
        while result != 1:
            result = collatz(result)

apply_collatz()

#!/usr/bin/python3
for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print(f"FizzBuzz ", end="")
    elif num % 3 == 0:
        print(f"Fizz ", end="")
    elif num % 5 == 0:
        print(f"Buzz ", end="")
    else:
        print(f"{num} ", end="")

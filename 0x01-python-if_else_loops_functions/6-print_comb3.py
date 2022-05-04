#!/usr/bin/python3
for numbers in range(0, 10):
    for numbers2 in range(0, 10):
        if numbers < numbers2 and numbers != numbers2 and numbers < 8:
            print(f"{numbers}{numbers2}", end=", ")
print(89)

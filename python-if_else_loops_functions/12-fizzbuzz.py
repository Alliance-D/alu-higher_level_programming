#!/usr/bin/python3
# fizzbuzz
def fizzbuzz():
    for i in range(100):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz ")
        elif i % 3 == 0:
            print("Fizz ")
        elif i % 5 == 0:
            print("Buzz ")
        else:
            print("{}".format(i))

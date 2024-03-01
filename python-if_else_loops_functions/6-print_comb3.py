#!/usr/bin/python3
#prints possible combinations of 2 digit numbers
for i in range(10):
        for j in range(i + 1, 10):
            if i != 8 or j !=9 and i != j:
               print(f"{i}{j}", end=", ")
            else:
                print(f"{i}{j}\n")

#!/usr/bin/python3

for i in range(100):
    if i == 99:
        print("{:12d}".format(i))
    else:
        print("{:12d}".format(i), end=", ")

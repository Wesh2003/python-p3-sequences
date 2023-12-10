#!/usr/bin/env python3

def print_fibonacci(length):
    f = 0
    g = 1

    if length<0:
        return []
    elif length == 0:
        return [] 
    elif length == 1:
        return g 
    else: 
        for i in range (2, length):
            j = f + g 
            f = g 
            g = j 
        return g 

print_fibonacci(9)


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary = str(bin(n)[2:])
    sum_lst = []
    i = 0
    while i < len(binary):
        sum_1 = 0
        if binary[i] == "1":
            j = i + 1
            sum_1 += 1
            if j < (len(binary) - 1):
                while binary[j] == "1":
                    sum_1 += 1
                    j=j+1
                    if j == len(binary):
                        break
            sum_lst.append(sum_1)
            i = j
        else:
            i = i+1

    print(int(max(sum_lst)))

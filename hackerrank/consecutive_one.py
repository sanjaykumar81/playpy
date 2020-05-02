#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    number = '{0:b}'.format(n)

    max_consecutive =0
    consecutive_one =0
    for i in number:

        if i =='1':
            consecutive_one +=1

            if consecutive_one > max_consecutive:
                max_consecutive = consecutive_one
        else:
            consecutive_one = 0

    print(max_consecutive)

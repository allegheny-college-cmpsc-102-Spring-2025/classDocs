#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Frequency table for a list of numbers
'''
from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
        # print(f"number : {number}"),
        print('value: {0}\tfreq: {1}'.format(number[0], number[1]))

if __name__=='__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    print("fScores :{scores}")
    frequency_table(scores)
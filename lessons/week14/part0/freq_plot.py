#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Frequency table for a list of numbers, make a plot of frequencies
'''
from collections import Counter
import matplotlib.pyplot as plt

def frequency_table(numbers:list) -> list:
    table = Counter(numbers)
    print('Number\tFrequency')
    char_list = [] # characters
    freq_list = [] # freqs of characters
    for number in table.most_common():
        # print(f"number : {number}"),
        print('value: {0}\tfreq: {1}'.format(number[0], number[1]))
        char_list.append(number[0])
        freq_list.append(number[1])
    return char_list, freq_list
# end of frequency_table()

def plot_character_frequencies(char_list, freq_list):
    # Prepare data for plotting
    # characters = list(char_freq.keys())
    # frequencies = list(char_freq.values())
    
    # Plotting
    plt.bar(char_list, freq_list)
    plt.title('Character Frequencies')
    plt.xlabel('Character')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()
# end of plot_character_frequencies()
    

if __name__=='__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    print("fScores :{scores}")
    char_list, freq_list = frequency_table(scores)
    plot_character_frequencies(char_list, freq_list)
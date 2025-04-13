#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_corr_x_y(x,y):
    """ Determine correlation"""

    n = len(x)
    # Find the sum of the products
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []

    for xi in x:
        x_square.append(xi**2)

    # Find the sum
    x_square_sum = sum(x_square)

    y_square=[]

    for yi in y:
        y_square.append(yi**2)

    # Find the sum
    y_square_sum = sum(y_square)

    # Use formula to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    print(f"\tCorrelation : {correlation}")


if __name__ == '__main__':
    grades_list = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
    scores_list = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
    print(f"\t grades : {grades_list} ")
    print(f"\t scores : {scores_list}")
    find_corr_x_y(grades_list, scores_list)

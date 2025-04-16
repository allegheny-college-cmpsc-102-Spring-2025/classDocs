#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# To run, you will need to install the following libraries
# matplotlib
# plotly
# pandas

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
    print(f"\t Correlation : {correlation}")

def scatterPlot(x_list : list, y_list:list) -> None:
    """ prepare a scatter plot of the inputted data """
    plt.scatter(x_list, y_list)
    plt.show()

    # end of scatterPlot()

def dataMaker():
    """ prepare random but correlated data to test."""

    # Set seed for reproducibility
    np.random.seed(42)

    # Generate 1000 correlated numbers
    mean = 0
    std_dev = 1
    num_samples = 1000

    # Generate correlated numbers
    x = np.random.normal(mean, std_dev, num_samples)
    print(f" X data: {x}")
    # Add some noise
    noise = np.random.normal(0, 0.1, num_samples)  # Adjust the standard deviation of noise as needed
    y = x + noise
    print(f" Y data: {y}")
    return x, y
# end of datamaker()


def plotlyScatterPlot(x_list : list, y_list:list) -> None:
    fig = px.scatter(x = x_list, y = y_list)
    fig.show()
# end of plotlyScatterPlot()

if __name__ == '__main__':
    # grades_list = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
    # scores_list = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
    # print(f"\t grades : {grades_list} ")
    # print(f"\t scores : {scores_list}")

    x_list, y_list = dataMaker()

    find_corr_x_y(x_list, y_list)
    plotlyScatterPlot(x_list, y_list) # use plotly to interact with the data
    scatterPlot(x_list, y_list) # create static plot
    
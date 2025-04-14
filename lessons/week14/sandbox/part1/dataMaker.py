#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

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

# Print correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]
print("Correlation coefficient:", correlation_coefficient)


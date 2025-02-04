
# setup virtual environment
# python3 -m venv myenv
# source myenv/bin/activate
# pip3 install matplotlib

import matplotlib.pyplot as plt
import math

# get factorial data

x_list = [i for i in range(10)]
factorials_list = [math.factorial(x) for x in x_list]
print("x,factorial(x)")
for i in range(len(x_list)):
	print(f"{x_list[i]},{factorials_list[i]}")

# formatting data
for i in range(len(x_list)):
	xvalue_int = x_list[i]
	fvalue_int = factorials_list[i]
	print("%s, %s" % (xvalue_int,fvalue_int))


# prepare plot
	
print(f"xlist :{x_list}")
print(f"factorials_list : {factorials_list}")
plt.plot(x_list, factorials_list)
plt.xlabel('x value')
plt.ylabel('factorial(x)')
plt.show()

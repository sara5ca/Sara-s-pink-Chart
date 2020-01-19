""" DOTART """

import matplotlib.pyplot as plt import numpy as np import random

plt.axis([10,140,90,-10])

plt.axis('off') plt.grid(False)

plt.arrow(0,0,20,0,head_length=20,head_width=10,color='k') plt.arrow(0,0,20,20,head_length=20,head_width=30,color='k')
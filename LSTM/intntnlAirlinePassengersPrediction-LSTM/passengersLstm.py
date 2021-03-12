# Import the required libraries
from matplotlib import pyplot as plt
import pandas as pd
import os

data = pd.read_csv('data/oldPassengers.csv', usecols=[1], engine='python')
plt.plot(data)
plt.show()
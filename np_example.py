# https://www.jetbrains.com/help/pycharm/2016.3/matplotlib-support.html
import matplotlib.pyplot as plt
import numpy as np

X = np.random.normal(0, 1, 1000)
print(X.mean(), X.std())

plt.hist(X)
plt.show()

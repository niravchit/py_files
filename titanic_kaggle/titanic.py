"""
Goal: to predict if a passenger survived the sinking of the Titanic or not. Statistically speaking, women, children and upper class had best
chance to survive. For each passenger in test set, you must predict 0 or 1 for the Survived variable

Submission: 418 entries plus a header row. 2 columns - PassengerID, Survived

"""
import pandas
import matplotlib as mpl
import seaborn
import scipy
from sklearn.linear_model import LinearRegression
import numpy as np 


# def velocity(t):
#     return (25 + 10.0*t)
# #integrate velocity to get distance
# distance = scipy.integrate.quad(velocity, 0, 3)
# print(distance)

print('hello')
#print(type(lambda x: x+1))

r = np.arange(36)
r.resize(6,6)
print(r.reshape(36))
print(r[2:4,2:4])
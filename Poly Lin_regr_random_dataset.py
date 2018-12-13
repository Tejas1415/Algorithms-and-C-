import random
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


import matplotlib.pyplot as plt

# How_many, how much each value should vary, approx how much gap should be there between values
# If correlation is pos, then values will benormal to apply linear regression, if its negative all values get scattered totally.
def create_dataset(hm, variance, step=2, correlation = False):
    val=1                                           # 1st value of y
    ys= []                                          # empty list
    for i in range(hm):
        y = val +  random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val+=step
        if correlation and correlation == 'neg':
            val-= step
        xs = [i for i in range(len(ys))]
    return np.array([xs], dtype=np.float).reshape((-1,1)), np.array(ys, dtype=np.float)

# creating the database

xs, ys = create_dataset(40, 20, 5, correlation='neg')
print(xs,ys)
# if the variance is increased, the points go further away from the regression line obviously, hence squarred error is more worse
# if the variance decreased, all values will be near to regression line, reducing squarred error, more accurate
# correlation just makes points values scatter upwards / downwards


# use linear regression and polynomial regression.
# Simple Linear Regression
linear_reg1 = LinearRegression(n_jobs=-1)
linear_reg1.fit(xs,ys)

# polynomial Linear Regression
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(xs)
# in poly function, x,x^2,x^3 etc will be there, all those values will be calculated in this step
linear_reg2 = LinearRegression()
linear_reg2.fit(X_poly,ys)

# Plot all the results

plt.figure(1)
plt.plot(xs,linear_reg1.predict(xs), color = 'r')
plt.scatter(xs,ys, color='b')
plt.show()

plt.figure(2)
plt.scatter(xs, ys, color = 'g')
plt.plot(xs,linear_reg2.predict(X_poly), color='b')
plt.show()

# To verify the accuracy and find the Root Mean Squared Values
from sklearn.metrics import mean_squared_error
from math import sqrt

rms1 = sqrt(mean_squared_error(ys,linear_reg1.predict(xs)))
print(rms1)

rms2 = sqrt(mean_squared_error(ys,linear_reg2.predict(X_poly)))
print(rms2)

# Root mean Square error is around 23% in this case, best fit is degree 2.


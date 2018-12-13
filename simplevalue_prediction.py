import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
from sklearn import cross_validation

# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
X = np.array([1999,2002,1993,1900,2005,1990]).reshape((-1, 1))
# Using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
# Here,its only one feature
y = np.array([10, 20, 11, 15, 3, 6])
print(X, type(X))
print(len(X), len(y))

# Just plotting the input data.
# Not required in this program though.
plt.scatter(X,y)
plt.ylabel("features")
plt.xlabel("some values")
plt.show()

# Fit the model
clf = LinearRegression()
clf.fit(X, y)

# Predict the values
print(clf.predict([[1992]]))   # Remember to use double square brackets.
print(clf.predict([[2002]]))


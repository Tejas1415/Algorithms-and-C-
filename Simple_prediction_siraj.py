from sklearn import tree

#[height, weight, shoe size]
X = [[100, 30, 5], [130, 60, 7], [150, 76, 6], [111, 80, 8], [170, 100, 9]]
y = ['male', 'female', 'male', 'male', 'female']

clf = tree.DecisionTreeClassifier()
clf.fit(X,y)

prediction = clf.predict([[120, 92, 7]])
print(X, prediction)

# Now let us test the same for height is male is given
# you cannot use a string during machine learning
#convert that into a number through autoencoder/ one hot encoding before you use in the real world programming.

X1 = [['male', 30, 5], ['female', 60, 7], ['male', 76, 6], ['male', 80, 8], ['female', 100, 9]]
y1 = [100, 130, 150, 111, 170]

clf1 = tree.DecisionTreeClassifier()
clf1.fit(X1,y1)

prediction1 = clf1.predict([['male', 92, 7]])
print(prediction1)

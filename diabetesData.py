import numpy as np
import pandas as pd
import sklearn as sk
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFile = pd.read_csv (r'/Users/coreyrice/Desktop/Datamining/pima-indians-diabetes.csv', names = names)
from sklearn import metrics
from numpy import where
from numpy import unique
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")
stdScaler = StandardScaler()

#Set up x and y
X = dataFile[['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']]
Y = dataFile['class']
SScaled = stdScaler.fit_transform(X)
nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
nn.fit(X,Y)

print("Unscaled Data")

scores = cross_val_score(nn, X, Y, cv=5, scoring='accuracy')
print(scores.mean())
scores = cross_val_score(nn, X, Y, cv=5, scoring='recall')
print(scores.mean())
scores = cross_val_score(nn, X, Y, cv=5, scoring='precision')
print(scores.mean())
scores = cross_val_score(nn, X, Y, cv=5, scoring='f1_macro')
print(scores.mean())

print("Scaled Data")
scores = cross_val_score(nn, SScaled, Y, cv=5, scoring='accuracy')
print(scores.mean())
scores = cross_val_score(nn, SScaled, Y, cv=5, scoring='recall')
print(scores.mean())
scores = cross_val_score(nn, SScaled, Y, cv=5, scoring='precision')
print(scores.mean())
scores = cross_val_score(nn, SScaled, Y, cv=5, scoring='f1_macro')
print(scores.mean())

x, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0,
                           n_clusters_per_class=1, random_state=4)
model = KMeans(n_clusters=2)
yhat = model.fit_predict(x)
clusters = unique(yhat)
for cluster in clusters:
    row_ix = where(yhat == cluster)
    plt.scatter(x[row_ix, 0], x[row_ix,1])
    
plt.show()
# -*- coding: utf-8 -*-
"""1_i.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18TgWrVvUnC6TycdkWoPYcdzJrH5b32uy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file= pd.read_csv("./Dataset.csv",header=None,float_precision='round_trip')

plt.scatter(file[0], file[1])
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Data points before centering")
plt.show()

mean_x=file[0].mean()
mean_y=file[1].mean()

file[0]=file[0] - mean_x
file[1]=file[1] - mean_y

plt.scatter(file[0], file[1])
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Data points after centering")
plt.show()

X=file.transpose()

C=np.dot(X,X.transpose())/len(X.transpose()) #C is the Covariance Matrix

from numpy.lib.twodim_base import triu_indices
e_values, e_vectors = np.linalg.eig(C)
z=e_values, e_vectors
e_v=e_vectors.transpose()  #[[w1x w1y][w2x w2y]]
  
pair=[]
for i in range(0,2):
  t=e_values[i],e_v[i]
  pair.append(t)

pair.sort(reverse=True)

w_=[]
e_vals=[]
for i in pair:
  w_.append(i[1])
  e_vals.append(i[0])

w__ = np.array(w_)
w=w__.transpose() #[[w1x,w2x],[w1y, w2y]]

xtw=np.dot(X.transpose(),w) #dimensions: 1000x2

xtw1=xtw[:,0].reshape(1000,1)
xtw2=xtw[:,1].reshape(1000,1)

proxies_w1=w[0]*xtw1
proxies_w2=w[1]*xtw2

plt.plot(proxies_w1[:,0],proxies_w1[:,1],label="w1")
plt.plot(proxies_w2[:,0],proxies_w2[:,1],label="w2")
plt.legend(loc="best")
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("PCA with centering")
plt.show()

variance1=e_vals[0]/(e_vals[0]+e_vals[1])
print(variance1) #variance explained by the first principal component

variance2=e_vals[1]/(e_vals[0]+e_vals[1])
print(variance2) #variance explained by the second principal component
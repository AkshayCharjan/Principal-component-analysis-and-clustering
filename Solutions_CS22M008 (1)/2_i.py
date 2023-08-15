# -*- coding: utf-8 -*-
"""2_i.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dl4ax2D16deHNj5YQNGZPn9Yq7CIV3-S
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file= pd.read_csv("./Dataset.csv",header=None,float_precision='round_trip')
cluster = np.zeros(1000)
X=file.transpose()

def find_mean(c,cluster):   #finds mean of the cluster c
    Sum_x=0
    Sum_y=0
    n=0
    for i in range(0,1000):
            if(cluster[i]==c):
                Sum_x+=X[i][0]
                Sum_y+=X[i][1]
                n+=1         
    mean_x=Sum_x/n             
    mean_y=Sum_y/n
    mean= np.zeros((2))
    mean[0]=mean_x
    mean[1]=mean_y
    return mean

#1

cluster=np.random.randint(1,5,1000)
mean_c=np.zeros((4+1,2))
cluster_update=cluster.copy()
flag=1
flagC=1
starting_flag=True
ErrorV=[]
while(starting_flag or np.any(cluster!=cluster_update)):
    starting_flag=False
    cluster=cluster_update.copy()
    for i in range(1,5):
        mean_c[i]=find_mean(i,cluster)
    distance = np.zeros(5)
    E=0
    for i in range (0,1000):
        temp=X[i]-mean_c[cluster[i]]
        E+=np.linalg.norm(temp)
        dist=np.zeros((1,2))
        for j in range (1,5):
            dist[0]=X[i]-mean_c[j]
            distance[j]=np.linalg.norm(dist[0])
        min_=distance[cluster[i]]
        min_index=cluster[i]
        for m in range(1,5):
            if(distance[m]<min_):
                min_index=m
                min_=distance[m]        
        cluster_update[i]=min_index
    ErrorV.append(E)
for i in range(0,1000):
    if(cluster[i]==1):
        plt.scatter(X[i][0],X[i][1],color = '#88c999' )
        
    if(cluster[i]==2):
        plt.scatter(X[i][0],X[i][1],color = 'red' )
       
    if(cluster[i]==3):
        plt.scatter(X[i][0],X[i][1],color = 'purple' )
        
    if(cluster[i]==4):
        plt.scatter(X[i][0],X[i][1],color = 'green' )
       
plt.xlabel("x values")
plt.ylabel("y values")

plt.title("Clustering with k=4 Random Initialization 1")
plt.show()
plt.plot(ErrorV,color = 'green')  
plt.xlabel("Iteration")
plt.ylabel("Error Function")
plt.show()

#2

cluster=np.random.randint(1,5,1000)
cluster_update=cluster.copy()
flag=1
flagC=1
starting_flag=True
ErrorV=[]
while(starting_flag or np.any(cluster!=cluster_update)):
    starting_flag=False
    cluster=cluster_update.copy()
    for i in range(1,5):
        mean_c[i]=find_mean(i,cluster)
    distance = np.zeros(5)
    E=0
    for i in range (0,1000):
        temp=X[i]-mean_c[cluster[i]]
        E+=np.linalg.norm(temp)
        dist=np.zeros((1,2))
        for j in range (1,5):
            dist[0]=X[i]-mean_c[j]
            distance[j]=np.linalg.norm(dist[0])
        min_=distance[cluster[i]]
        min_index=cluster[i]
        for m in range(1,5):
            if(distance[m]<min_):
                min_index=m
                min_=distance[m]        
        cluster_update[i]=min_index
    ErrorV.append(E)
for i in range(0,1000):
    if(cluster[i]==1):
        plt.scatter(X[i][0],X[i][1],color = '#88c999' )
    if(cluster[i]==2):
        plt.scatter(X[i][0],X[i][1],color = 'red' )
    if(cluster[i]==3):
        plt.scatter(X[i][0],X[i][1],color = 'purple' )
    if(cluster[i]==4):
        plt.scatter(X[i][0],X[i][1],color = 'green' )
plt.xlabel("x values")
plt.ylabel("y values")

plt.title("Clustering with k=4 Random Initialization 2")
plt.show()
plt.plot(ErrorV,color = 'green')  
plt.xlabel("Iteration")
plt.ylabel("Error Function")
plt.show()

"""3"""

cluster=np.random.randint(1,5,1000)
cluster_update=cluster.copy()
flag=1
flagC=1
starting_flag=True
ErrorV=[]
while(starting_flag or np.any(cluster!=cluster_update)):
    starting_flag=False
    cluster=cluster_update.copy()
    for i in range(1,5):
        mean_c[i]=find_mean(i,cluster)
    distance = np.zeros(5)
    E=0
    for i in range (0,1000):
        temp=X[i]-mean_c[cluster[i]]
        E+=np.linalg.norm(temp)
        dist=np.zeros((1,2))
        for j in range (1,5):
            dist[0]=X[i]-mean_c[j]
            distance[j]=np.linalg.norm(dist[0])
        min_=distance[cluster[i]]
        min_index=cluster[i]
        for m in range(1,5):
            if(distance[m]<min_):
                min_index=m
                min_=distance[m]        
        cluster_update[i]=min_index
    ErrorV.append(E)
for i in range(0,1000):
    if(cluster[i]==1):
        plt.scatter(X[i][0],X[i][1],color = '#88c999' )
    if(cluster[i]==2):
        plt.scatter(X[i][0],X[i][1],color = 'red' )
    if(cluster[i]==3):
        plt.scatter(X[i][0],X[i][1],color = 'purple' )
    if(cluster[i]==4):
        plt.scatter(X[i][0],X[i][1],color = 'green' )
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Clustering with k=4 Random Initialization 3")
plt.show()
plt.plot(ErrorV,color = 'green')  
plt.xlabel("Iteration")
plt.ylabel("Error Function")
plt.show()

#4

cluster=np.random.randint(1,5,1000)
cluster_update=cluster.copy()
flag=1
flagC=1
starting_flag=True
ErrorV=[]
while(starting_flag or np.any(cluster!=cluster_update)):
    starting_flag=False
    cluster=cluster_update.copy()
    for i in range(1,5):
        mean_c[i]=find_mean(i,cluster)
    distance = np.zeros(5)
    E=0
    for i in range (0,1000):
        temp=X[i]-mean_c[cluster[i]]
        E+=np.linalg.norm(temp)
        dist=np.zeros((1,2))
        for j in range (1,5):
            dist[0]=X[i]-mean_c[j]
            distance[j]=np.linalg.norm(dist[0])
        min_=distance[cluster[i]]
        min_index=cluster[i]
        for m in range(1,5):
            if(distance[m]<min_):
                min_index=m
                min_=distance[m]        
        cluster_update[i]=min_index
    ErrorV.append(E)
for i in range(0,1000):
    if(cluster[i]==1):
        plt.scatter(X[i][0],X[i][1],color = '#88c999' )
    if(cluster[i]==2):
        plt.scatter(X[i][0],X[i][1],color = 'red' )
    if(cluster[i]==3):
        plt.scatter(X[i][0],X[i][1],color = 'purple' )
    if(cluster[i]==4):
        plt.scatter(X[i][0],X[i][1],color = 'green' )
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Clustering with k=4 Random Initialization 4")
plt.show()
plt.plot(ErrorV,color = 'green')  
plt.xlabel("Iteration")
plt.ylabel("Error Function")
plt.show()

#5

cluster=np.random.randint(1,5,1000)
cluster_update=cluster.copy()
flag=1
flagC=1
starting_flag=True
ErrorV=[]
while(starting_flag or np.any(cluster!=cluster_update)):
    starting_flag=False
    cluster=cluster_update.copy()
    for i in range(1,5):
        mean_c[i]=find_mean(i,cluster)
    distance = np.zeros(5)
    E=0
    for i in range (0,1000):
        temp=X[i]-mean_c[cluster[i]]
        E+=np.linalg.norm(temp)
        dist=np.zeros((1,2))
        for j in range (1,5):
            dist[0]=X[i]-mean_c[j]
            distance[j]=np.linalg.norm(dist[0])
        min_=distance[cluster[i]]
        min_index=cluster[i]
        for m in range(1,5):
            if(distance[m]<min_):
                min_index=m
                min_=distance[m]        
        cluster_update[i]=min_index
    ErrorV.append(E)
for i in range(0,1000):
    if(cluster[i]==1):
        plt.scatter(X[i][0],X[i][1],color = '#88c999' )
    if(cluster[i]==2):
        plt.scatter(X[i][0],X[i][1],color = 'red' )
    if(cluster[i]==3):
        plt.scatter(X[i][0],X[i][1],color = 'purple' )
    if(cluster[i]==4):
        plt.scatter(X[i][0],X[i][1],color = 'green' )
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Clustering with k=4 Random Initialization 5")
plt.show()
plt.plot(ErrorV,color = 'green')  
plt.xlabel("Iteration")
plt.ylabel("Error Function")
plt.show()
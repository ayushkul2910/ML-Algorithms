import csv
import numpy as np
import math
import random as rd
import matplotlib.pyplot as plt

#function for finding distance between test point and a data point
def distance(test,data):
    m=len(test)
    d=0
    for i in range(m):
       d+=(test[i]-data[i])**2
    return math.sqrt(d)

#function for finding majority of a class
def mode(A):
    return max(set(A),key=A.count)


#function for splitting the dataset into train-test ratio
def split(X,y,size):
    X_train=[]
    y_train=[]
    X_test=[]
    y_test=[]
    index_train=[]
    index_test=[]
    while(len(index_train)!=int(len(X)*(1-size))):
        a=rd.randint(0,len(X)-1)
        if a not in index_train:
            index_train.append(a)

    for i in range(0,len(X)):
        if i not in index_train:
            index_test.append(i)
            
    for i in index_train:
        X_train.append(X[i])
        y_train.append(y[i])
        
    for i in index_test:
        X_test.append(X[i])
        y_test.append(y[i])

    return X_train,X_test,y_train,y_test
        

X=[]
y=[]
with open('iris.csv') as f:
    file=csv.reader(f)
    for row in file:
        X.append([float(row[0]),float(row[1]),float(row[2]),float(row[3])])
        y.append(row[4])

X=np.array(X)
y=np.array(y)
y_plot=[]

lim=101

#iteration for all possible k values 
for k in range(1,lim):
    
    X_train,X_test,y_train,y_test=split(X,y,0.3)

    y_pred=[]
    
    for test in X_test:
        dist=[]
        for i in range(len(X_train)):
            dist.append((distance(test,X_train[i]),i))
        dist=sorted(dist,key=lambda x:x[0])
        final=[]
        for i in range(k):
            final.append(dist[i][1])

        final_class=[]

        for i in final:
            final_class.append(y_train[i])

        y_pred.append(mode(final_class))

    #Calculating accuracy of the algorithm
    score=0
    for i in range(len(y_pred)):
        if(y_pred[i]==y_test[i]):
            score+=1

    acc=float(score)/len(y_pred)
    print("K="+str(k)+" Accuracy="+str(round(acc,12)))
    y_plot.append(round(acc,12))
    
X_plot=[i for i in range(1,lim)]

plt.plot(X_plot,y_plot)
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.show()

import csv
import random as rd
import numpy as np

try:
    def distance(x,y):
        d=0
        for i in range(len(x)):
            if(x[i]!=y[i]):
                d+=1
            else:
                pass
        return d


    def mode(A):
        return max(set(A),key=A.count)


    def check_mode(L):
        Z=[]
        m=L.shape
        for i in range(m[1]):
            s=list(L[:,i])
            Z.append(mode(s))
        return Z
            

    l=[]

    with open('Kmode.csv') as f:
        file=csv.reader(f)
        for row in file:
            l.append(row)

    #print(l)

    print("Enter the value of K:")
    k=int(input())

    q=[]
    while(len(q)!=k):
        a=rd.randint(0,len(l)-1)
        if a not in q:
            q.append(a)

    ##q=[0,4,11,14]
    print("Initial Random Centroids:",q)
    print("\n")
    C=[]
    centroid=[]

    for i in q:
        centroid.append(l[i])

    C.append(centroid)
    #print(centroid)
    count=1

    while(True):
        dist=[]

        for i in l:
            d=[]
            for j in centroid:
                d.append(distance(i,j))
            dist.append(d)

        #print(dist)

        cluster=[]

        for i in range(k):
            c=[]
            cluster.append(c)

        for h,j in enumerate(dist):
            for g,i in enumerate(j):
                if(i==min(j)):
                    cluster[g].append(h)
                    break

        print("Iteration:",count)
        print(cluster)
        print("\n")

        centroid=[]
        
        for i in cluster:
            W=[]
            for j in i:
                W.append(l[j])
            W=np.array(W)
            res=check_mode(W)
            centroid.append(res)
        #print(centroid)
        C.append(centroid)
        if(C[count]==C[count-1]):
            break
        count+=1

except Exception as e:
    print(e)

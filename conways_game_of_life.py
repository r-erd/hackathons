H=range
import numpy as G

def c(p, r):
    if p==[]or p==None:return[]
    I=G.array(p);J=[r,r];L,M=I.max(0)+J;B,C=I.min(0)-J
    for r in H(0,r):
        print(r);K=[]
        for D in H(B-1,L+2):
            for E in H(C-1,M+2):
                F=0;N=1 if(D,E)in p else 0
                for O in [-1,0,1]:
                    for P in [-1,0,1]:
                        if(D+O,E+P)in p:F+=1
                if F==4 and N==1 or F==3:K.append((D,E))
        p=K
    A=G.array(p);B,C=A.min(0);A[:,0],A[:,1]=A[:,0]-B,A[:,1]-C;return list(map(tuple,A))
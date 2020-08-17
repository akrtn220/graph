import numpy as np

def saikoro1(P):
    x=1
    p=0
    for i in range(0,P):
        n=np.random.rand()
        # print(i)
        if x==1:
            if  n<=0.25:
                x=2 
                p+=10
            else:
                x=1
        else:
            if  n<=0.9:
                x=1 
                p-=15
            else:
                x=2
                p-=15

        # print(str(x)+' ',end="")     
    print('price1:'+str(p))
def saikoro2(P):
    x=1
    p=0
    for i in range(0,P):
        n=np.random.rand()
        # print(i)
        if x==1:
            if  n<=0.25:
                x=2 
                p+=10
            else:
                x=1
        else:
            if  n<=0.8:
                x=1 
                p-=10
            else:
                x=2
                p-=10

        # print(str(x)+' ',end="")     
    print('price2:'+str(p))

for j in range(0,100):
    saikoro1(100)
print(" ")
for k in range(0,100):
    saikoro2(100)

import numpy as np
x=1
while x!=5:
    print(str(x)+' ',end="")
    p=np.random.rand()
    if x==1:
        if p<0.8:
            x=2
        elif p<0.9:
            x=3
        else:
            x=4
    elif x==2:
        x=4
    elif x==3:
        if p<0.9:
            x=2
        else:
            x=5
    elif x==4:
        if p<0.8:
            x=3
        else:
            x=5

    
print(x)
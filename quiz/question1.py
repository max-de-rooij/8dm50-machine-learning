import numpy as np
def question1(a):
    rows=3
    columns=3
    A=np.zeros((3,3))
    for i in range(rows):
        for j in range(columns):
            A[i][j]=a
            a=a+1

    print(A)

question1(3)
        


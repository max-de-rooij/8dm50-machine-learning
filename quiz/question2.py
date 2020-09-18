import numpy as np
def question2(A):
    for k in A:
        if k>=0:
            k=np.arange(A,dtype=np.uint16)
        print(A)
        else:
            return A

question2(np.array([10.2,3.1,9.33]))
def greaterThan(L,n):
    L1=[];
    for i in range(len(L)):
        if(L[i]>n):
            L1.append(L[i]);
    return L1;
L=[1,2,3,4,5,6,7,8,9];
print(greaterThan(L,5));
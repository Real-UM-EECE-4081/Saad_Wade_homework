n=int(input("Please enter a non-negative integer:"))

fact=1

for i in range(1,n+1):

    fact = fact*i

print("The factorial of ",n," is ",fact,sep="")
def mymod(user,factor):
    a = user // factor
    b = user % factor
    return(a,b)

p = int(input("Enter a number :"))
isPrime = True

n = 2
while isPrime == True and n < p:
    c,r = mymod(p,n)
    if r !=0:
        isPrime=True
    else:
        isPrime = False
    

    n +=1
    
print(isPrime)


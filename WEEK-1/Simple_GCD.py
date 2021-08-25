# In this program we iterate from 1 to m with iterator i, if which, it yeilds 0 as remainder, we add it to the factors of m in fm list.
# Similarly we do for n and store it in fn.
# we compare fm and fn for common factors, if we found any, we store it on another list called cf.
# We then return the last element of the cf list because, the resulting list is ascending order, and we want greatest common factor, which will be available in the last index

def gcd(m,n):
    fm = []
    for i in range(1,m+1):
        if (m % i) == 0:
            fm.append(i)
    fn = []
    for j in range(1,n+1):
        if (n % j) == 0:
            fn.append(j)
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])

# driver code
print(gcd(8,6))

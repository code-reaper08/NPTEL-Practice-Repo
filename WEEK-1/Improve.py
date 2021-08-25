# We are going to improvre the Simple_GCD.py here

# Improvement 1:

# we can scan single time from 1 to max(m,n) and for each i in max(m,n), we can add i if it divides m and n without any remainders.

def gcd(m,n):
    fm = []
    fn = []
    for i in range(1,max(m,n)): #single loop instead of two for loops.
        if (m % i) == 0:
            fm.append(i) # add to fm
        elif ( n % i) == 0:
            fn.append(i) # add to fn
    cf = []
    for f in fm:
        for f in fn:
            cf.append(f) # add to cf
    return(cf[-1])

# driver code
print(gcd(18,72))


# Improvement 2:

# def gcd(m,n):
#     cf = []
#     for i in range(1,min(m,n)+1):
#         if (m%i) == 0 and (n%i) == 0:
#             cf.append(i)
#     return(cf[-1])

# # driver code
# print(gcd(18,72))
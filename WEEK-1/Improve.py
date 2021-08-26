# We are going to improvre the Simple_GCD.py here

# Improvement 1:

# we can scan single time from 1 to max(m,n) and for each i in max(m,n), we can add i if it divides m and n without any remainders.

def gcd(m,n):
    fm = []
    fn = []
    cf = []
    for i in range(1,max(m,n)): #single loop instead of two for loops.
        if (m % i) == 0:
            fm.append(i) # add to fm
        if ( n % i) == 0:
            fn.append(i) # add to fn
    for f in fm:
        if f in fn:
            cf.append(f) # add to cf
    return(cf[-1])

# driver code
print(gcd(98,56))


# Improvement 2:

def gcd(m,n):
    cf = []
    for i in range(1,min(m,n)+1): # common factor must be less than min(m,n)
        if (m%i) == 0 and (n%i) == 0: # logical and is used to check two conditions at once.
            cf.append(i)
    return(cf[-1])

# driver code
print(gcd(98,56))

# Improvement 3:

# Here we don't use lists at all!

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i # Most Recent Common Factor.
    return(mrcf)

# driver code
print(gcd(98,56))

# Improvemnent 4:

# Scanning backwards, from min(m,n) to 1 and not vice versa. Here First common factor we find will be GCD.

def gcd(m,n):
    i = min(m,n)
    while i>0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i = i-1

# driver code
print(gcd(98,56))
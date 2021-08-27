# Here we discuss about Euclid's algorithm for finding GCD.

# 1. using recursion:

def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n)
    else:
        return(gcd(n,m%n)) # recursive call

# driver code
print(gcd(98,56))

# 2. Using While loop:

def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    while (m%n) != 0:  # While checking for contradicting statement, to end itself.
        (m,n) = (n,m%n)
    return(n)

# driver code
print(gcd(98,56))
def factors(n):
    a = []
    for i in range(1,n+1):
        if n % i :
            a.append(i)
    return a 

def prime_check(n):
    return(factors(n) == [1,n])

prime_check(5)
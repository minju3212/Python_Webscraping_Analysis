def find_primes(start,end):
    primes = []
    for num in range(start+1,end):
        if prime(num):
            primes.append(num)
    return primes

def prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
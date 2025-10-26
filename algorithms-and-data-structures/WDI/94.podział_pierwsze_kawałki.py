
def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3 or n == 5: return True
    if not n % 2 or not n % 3 or not n % 5: return False
    i = 7
    while i*i <= n:
        if n % i == 0: return False
        i += 4
        if n % i == 0: return False
        i += 2
    return True

def divide(n):
    def rek(n,i,cnt):
        if is_prime(n) and is_prime(cnt):
            return True
        if i > n: return False
        if is_prime(n%i):
            if rek(n//i,10,cnt+1):
                return True
        return rek(n,10*i,cnt)

    return rek(n,10,1)

print(divide((222)))

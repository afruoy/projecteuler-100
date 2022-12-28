def solution(N=600851475143):

    s = set()
    def isPrime(n):
        for i in range(2, int(n**0.5)):
            if not n % i:
                return False
        return True

    for i in range(2, int(N**0.5)):
        if isPrime(i) and not N % i:
            s.add(i)
            N //= i             

    return max(s)
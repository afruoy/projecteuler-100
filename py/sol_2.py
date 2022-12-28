def solution(lim=4_000_000):
	cnt = 0
	fib_i = 1
	fib_ip1 = 2
	
	while fib_ip1 < lim:
		cnt += fib_ip1 if not fib_ip1%2 else 0 
		fib_i,fib_ip1 = fib_ip1, fib_i+fib_ip1 
	
	return cnt

print(solution())

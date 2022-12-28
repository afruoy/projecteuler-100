#brute-force
def solution(lim=1000):
	cnt = 0
	for i in range(lim):
		if (not i%3) or (not i%5):
			cnt += i
	return cnt
		
#faster
def solution1(lim=1000):
	l = [0,0]
	cnt = 0
	s = set()
	while l[0] < lim or l[1] < lim:
		if l[0] < lim and l[0] % 3 == 0 and l[0] not in s:
			cnt += l[0]
			s.add(l[0])
		if l[1] < lim and l[1] % 5 == 0 and l[1] not in s:
			cnt += l[1]
			s.add(l[1])
		l[0] += 3
		l[1] += 5
		
	return cnt

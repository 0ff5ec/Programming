'''
Given a time in HH:MM format, find the next closest time permuting the digits. For example: input 12:25 will produce 12:52; input 23:59 will produce 23:59
'''
def sameList(alist,blist):
	for i in range(len(alist)):
		if alist[i] != blist[i]:
			return False
	return True
def minsTotime(min):
	min = min%1440
	h = min//60
	if h<10:
		h1,h2 = 0, h
	else:
		h1, h2 = h//10, h%10
	m = min%60
	if m<10:
		m1,m2 = 0, m
	else:
		m1,m2 = m//10,m%10
	return [h1,h2,m1,m2]
def findNextClosestTime(T):
	H,M = T.split(":")
	mins = int(H)*60 + int(M)
	h1 = int(H)//10
	h2 = int(H)%10
	m1 = int(M)//10
	m2 = int(M)%10
	t1 = sorted([h1,h2,m1,m2])
	for i in range(1,1441):
		tmp = minsTotime(mins+i)
		if sameList(sorted(tmp), t1):
			return str(tmp[0])+str(tmp[1])+':'+str(tmp[2])+str(tmp[3])
if __name__ == "__main__":
	print(findNextClosestTime(raw_input("Enter a time in HH:MM format= ")))

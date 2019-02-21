import time

testlist = []
for x in range(1,10000001,1):
	testlist.append(x)
#print(testlist)
while True:
	a=int(input(' Input angka yang ingin dicari : '))
	if a<75476476 and a>0:
		break
start = time.time()

def binarySearch(x, item):
	y = 0
	z = len(x)-1
	found = False
	
	while y<=z and not found:
		midpoint = (y + z)//2
		if x[midpoint]==item:
			found = True
		else:
			if item<x[midpoint]:
				z=midpoint-1
			else:
				y = midpoint+1
	return found
list_length=len(testlist)
print(binarySearch(testlist,(a)))
print(" Angka terdapat pada index ke-",testlist.index(a))
print(" Jumlah indeks = ",len(testlist))

end = time.time()
print (' Waktu eksekusi adalah = ',(end-start),' detik')
import time

testlist = []
for x in range(1,10000001,1):
	testlist.append(x)
#print(testlist)
while True:
	a=int(input("Masukkan Angka: "))
	if a<75476476 and a>0:
		break
start = time.time()

def linearS(a, item):
	x = 0
	y = 0
	z = len(a)-1
	found = False	
	while x<=z and not found:
		y+=1
		if a[y]==item:
			found = True
		else: x = x+1
list_length=len(testlist)
print("Angka terdapat pada indeks ke-",testlist.index(a))
print("Jumlah indeks = ",len(testlist))

end = time.time()
print ("Waktu eksekusi = ",(end-start)," detik")
k=0
N=int(input("masukkan orang dalam ruangan: "))
for i in range(1,N):
	for j in range(i,N):
		k+=1
print("jumlah jabat tangan yang terjadi:",k)
def hitungkembalian(tot,byr):
	if tot>byr:
		print('Maaf uang anda kurang')
		return
	kembalian=byr-tot
	listkembalian=[]
	sisa=divmod(kembalian,50000)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 50000')
	sisa=sisa[1]
	sisa=divmod(sisa,20000)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 20000')
	sisa=sisa[1]
	sisa=divmod(sisa,10000)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 10000')
	sisa=sisa[1]
	sisa=divmod(sisa,5000)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 5000')
	sisa=sisa[1]
	sisa=divmod(sisa,2000)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 2000')
	sisa=sisa[1]
	sisa=divmod(sisa,1000)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 1000')
	sisa=sisa[1]
	sisa=divmod(sisa,500)
	if sisa[0]>0:
		listkembalian.append(str(sisa[0])+' x 500')
	sisa=sisa[1]
	
	for x in range(len(listkembalian)):
		print(listkembalian[x])
	return 
	
hitungkembalian(1000,50000)
	
	
	
n = int(input("input parameter panjang persegi: "))
if n%2!=0 and n>3:
    print (' * '+' = '*int((n-2)/2)+' * '+' = '*int((n-2)/2)+' * ')
    for i in range(int(((n-2)/2))):
        print (' = '+' = '*int((n-2)/2)+' * '+' = '*int((n-2)/2)+' = ')
    print(' * ' * n)
    for i in range(int(((n-2)/2))):
        print (' = '+' = '*int((n-2)/2)+' * '+' = '*int((n-2)/2)+' = ')
    print (' * '+' = '*int((n-2)/2)+' * '+' = '*int((n-2)/2)+' * ')
else:
    print("input harus bilangan ganjil dan lebih dari 3")


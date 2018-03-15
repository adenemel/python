sayi = int(input("Kaçıncı fibonaççi sayısına kadar saymamızı istersiniz? : "))
sayi1=1
sayi2=1
n=0
for i in range (sayi):
    if (i==0):
        print (i)
    elif (i<3):
        print (1)
    else :
        print (sayi1+sayi2)     
        n=sayi2
        sayi2=sayi1+sayi2
        sayi1=n

sayi = int(input("Kaçıncı fibonaççi sayısına kadar saymamızı istersiniz? : "))
s1=1
s2=1
n=0
for i in range (sayi):
    if (i==0):
        print (i)
    elif (i<3):
        print (1)
    else :
        print (s1+s2)     
        n=s2
        s2=s1+s2
        s1=n

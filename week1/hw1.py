# week1
dongu = int(input("kaç işlem yapmak istersiniz"))
for i in range(0,dongu):
    sayi1 = int(input("Sayı1'i giriniz:"))
    sayi2 = int(input("Sayı2'i giriniz:"))
    islem = input("Yapılacak 4  işlemden birini seçiniz(+,-,/,*):")
    if islem == "+" :
        print (sayi1+sayi2)
    elif islem == "-" :
        print (sayi1-sayi2)
    elif islem == "*" :
        print (sayi1*sayi2)
    elif (islem == "/") & (sayi2==0):
        print ("Gecerli sayi girisi yapiniz")
    elif islem =="/" :
        print (sayi1/sayi2)
    elif islem == "exit":
        break
    else:
        print("4 işlemden birini giriniz.")

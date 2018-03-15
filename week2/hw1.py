import random
toplam1 = 0
toplam2 = 0
sonuc = 0
arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
    toplam1 = toplam1 + i

arr[0] = random.randint(1, 99)
print(arr)
toplam2 = toplam1 + arr[0]
sonuc = toplam2 - toplam1
print("\nDuplicate olan sayi : " + str(sonuc))

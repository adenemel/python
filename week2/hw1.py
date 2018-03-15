import random
t1 = 0
t2 = 0
sonuc = 0
arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
    t1 = t1 + i

arr[0] = random.randint(1, 99)
print(arr)
t2 = t1 + arr[0]
sonuc = t2 - t1
print("\nDuplicate olan sayi : " + str(sonuc))

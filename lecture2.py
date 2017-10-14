#While and For Loops and Function Defining

#while loop

n = int (input("enter numbers")) #kullanıcıdan input alıp, integer a cast ediliyor ve n değişkenine atanıyor.

total = 0   #total değerine 0 atanıyor.

while (n != 0):      #while döngüsünün devam etme şartı belirleniyor, n 0 olmadığı sürece bitmeyecek

    total += n       # n değeri >0 olduğu sürece her azaldığında yeniden total'a ekleniyor
    n-=1             #n > 0 olduğu sürece bir azaltılıyor
                     # while döngüsününde yapılacak işlemler bir tab içerde yazılıyor, scope alanı burası
print(total)         #döngü bittikten sonra, total değerini ekrana bas.

#for loop

for i in range(4,12):   #4 ten 12 ye kadar bir aralığa sahibiz 
    if(i%2== 0):        # 4 ile 12 arasındaki sayılardan çift olanları bul, ekrana bas.
        print(i)

#function defining
def f():
    #bi tab icerde yazinca scope a dahil
    #burada fonksiyonda yapılması istenen şeyler yer alıyor.
    #fonksiyona dahil olmasını istemediğimiz şeyleri scope alanının dışında yazmalıyız.

#function call
f()   #diğer programlama dillerinde olduğu gibi çağrılıyor

#Example 
x = input("enter a number")  #kullanıcıdan alınan değer
x = int(x)  #integer a cast ediliyor

#iç içe 2 for sayesinde kare matris gibi gözükecek

for i in range(0,x):  #aralık, 0 dan kullanıcıdan alınan değere kadar 
    for j in range(0,x): #0 dan kullanıcıdan alınan değere kadar
        if(i==j):
            print("1 ",end =" ")  #i ile j eşit olduğunda 1 olmadığında ekrana 0 bas
        else:
            print("0 ", end = " ")

    print("\n")

#kullanıcı 3 girdiğinde output şöyle oluyor
'''
100
010
001
'''



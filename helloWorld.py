# Introduction to Python

#degisken tanımlarken adını vermemiz yeterli, compiler tipinin ne olduğunu kendisi anliyor
# yani int, double, char, string gibi tipleri belirtmeden direkt olarak tanimlayabiliyoruz

x= 5
y = 10.3
z = "Hello World" 
gibi 

print("hello world!")  # ekrana bi şey basmak için print komutu kullaniyoruz, bu bir sayı ya da string olabilir. 
print(z)
print("duygu", "bulut", 2017)

print("hello", "world", sep=".")  # yazılan kelimeler arasina . koyarak yaziyor.
#output hello.world

#kullanicidan veri almak için ise input komutunu kullaniyoruz

#Example for area calculation
pi = 3.14  #burada pi değerine 3.14 ataniyor
diameter = input("Please enter diameter of radius > ") #kllanicidan diameter icin deger girmesi isteniyor
#find radius
#radius = int(diameter)/2  #sayi girsek bile karakter olarak algiliyor input, bu yuzden integer a cast ediliyor

#find area of circle
area = pi*(radius*radius)
print("area is > ", area)

# example for Pressure Calculation
g= 9.8

h = input("Please enter h value > ") #for height
d = input("Please enter d value > ") #for density

pressure = int (h) * int (d) * g  #pressure = height*density*gravity
print("Pressure is > " ,pressure)



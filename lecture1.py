#if -else conditions

a=5   # a icin 5 degerini atadik

b=6   # b icin 6 degerini atadik

if(a>b):    # eger a > b ise ekrana alttaki ifadeyi yaz ve a ile b yi toplayip c ye at.
    print("a is greater than b ")
    c= a+b
else:     #eger a > b degilse, ekrana alttaki ifadeyi yaz ve b den a yi cıkarip, c ye at.
    print("b is greater than a or a and b is equal")
    c = b -a

    print(c)  #c yi ekrana bas
    
#burada gordugunuz gibi {} yok, bir tab icerisi scope alani olarak kabul ediliyor. Yani kosul saglanirsa yapilmasini
#istedigimiz tum islemleri bi tab iceriden yaziyoruz, kosulla ilgili islemleri bitirip, kodlamaya devam etmek istedigimizde
#basa donup yazmaya devam ediyoruz.

#Basic Example
x= 50
if(x == 50)   #eger x 50 ise ekrana 50 yaziyor
    print("50 ")
    if(x < 75)  #bi tab iceride oldugu icin hala scope alanindayiz, 50 75 den kucuk oldugu icin bu if sarti da saglaniyor
        print(25)   #ekrana sırasiyla 50 ve 25 yaziyor
 
#Example 2 

print("enter an temperature value > ")
temp =input()  #kullanicidan bi temperature degeri aliyoruz 
temperature = int(temp)  #string olarak alinan degeri int e cast ediyoruz

if(temperature <= 0):    #hangi sarti saglarsa ekrana onunla ilgili kismi basiyor
    print("frozen ")
elif(temperature <=12):  #burada else kullansaydik, program sonlanirdi, bu yuzden else if kullaniyoruz
    print("cold ")
elif(temperature <=25):
    print("warm ")
elif(temperature <=75):
    print("hot ")
elif(temperature <=100):
    print("very hot ")
else:              #tum ihtimaller yazildiktan sonra son sart else olarak yazilabilir.
    print("burning")
       


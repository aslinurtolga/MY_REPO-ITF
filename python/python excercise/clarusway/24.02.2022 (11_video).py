# -*- coding: utf-8 -*-
"""24.02.2022(11.video).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O6EZx1COTryNDJ5W6bFFxTLawY55cgGW

İF - ELSE SATATEMENTS
if condition1
    execute body1
else:
    execute body2
*if else elif bi kod bloğudur. 
*eğer bu condition1 false, falsy verirse else devreye girer.
burada if else aynı hizadadır, çünkü bu else burada if e aittir.
"""

course = 'clarusway'
if course == "clarusway":
     print("you guaranteed the job")
else:
    print("think about it again")

number = 5
if number <= 3:
     print("Number is smaller than or equal to 3")
else: #optional clause (you can only have one else)
    print("Number is bigger than 3")

num = input("Enter a number":) #şimdi inputun içi string. biz str i integer a çevirebiliriz.
num = int(input("Enter a number:"))  #artık int çevirmiş olduk.

"""# ***BU KISIMDA ENTER KOD VAR DİKKAT ET !!!!!***
çalıştırınca kod istiyor.

1. soru gireceğimiz sayı çiftse ... is even yaz
değilse ... is odd yaz.

2. girilen sayının sonucu negatif ise negatif, pozitif ise pozitif versin.
YANİ ARTI BİR RAKAM GİRERSE POZİTİF
EKSİK RAKAM GİRERES NEGATİF ama sıfır girilmeyecek.
3. kullanıcıdan 2 tane rakam isteyeceğiz, sonra büyük olanı yazdıracağız.
4. boolean True to string value of "yes"
convert boolean False to string value of "no"
"""

# 1 sorunun cevabı
num = int(input("Enter a number:"))
if num %2 == 0 :                         ## (girilen sayının 2 ye bölümünden (modulus 2) kalan 0 ise bu sayı çift bir sayıdır, demiş olduk burada.)
    print("{} is even".format(num))
else:                                     #kalan tüm şartları kendi üzerinde topladığı için başka bir koşul girmedik.
    print("{} is odd".format(num))

0 % 2  # 0 ın modulus 2 si de 0 dır.

#2.sorunun cevabı
num = float(input("Enter a number except zero :")) #bu kez de float girdik integerda olur.
#sıfır haricinde bir rakam girilecek.
if num > 0 :
     print("It is a positive number.")
else :  # girilecek olan number>0 dışındaki her şey else nin koşulunu sağlar.
     print("Negative number")

num = float(input("Enter a number except zero :")) #bu kez de float girdik integerda olur.
#sıfır haricinde bir rakam girilecek.
if num > 0 :
     print("It is a positive number.")
else :  # girilecek olan number>0 dışındaki her şey else nin koşulunu sağlar.
     print("It is a Negative number")

#3. sorunun cevabı  iki tane rakam girilecek, büyük olanı alacak sistem.
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
if num1 > num2 :
     larger = num1
else :
     larger = num2
     print("The larger number is", larger)

#3. sorunun cevabı  iki tane rakam girilecek, büyük olanı alacak sistem. BU DA İKİNCİ ÇÖZÜM YOLU
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
if (num1 > num2) :
     print("The large number is", num1)
else :
     print("The large number is", num2)

# ASUMAN CA ENTER CODE 
bool_value = input("if answer :")
if bool_value :
   print("Yes")
else:
   print("No")

##   4.sorunun cevabı
bool_value = True         #Bu kısmı manuel olarak değiştiriyoruz.
if bool_value :                  #burada değişkenin yapısı boolean olduğu için direkt olarak if yapısının içinde kullanabiliyoruz. buna dikkat et.
    print("Yes")                  #kullanabilmemizin sebebi true doğru cevabını false ile yanlış cevabını verir, yapı itibariyle.
else : 
    print("No")

str(False)

"False" == str(False)

audience = "baby"

if audience == "kid" :
     print("it is free to go to cinema")
elif audience == "teen":
     print("discounted price!")
elif audience == "adult":
     print("normal price")
else :
     print("No such audience, stay at your home!")

# İF ELİF VE ELSE BLOĞU İLE İLGİLİ SORULAR
# kullanıcıya 3 tane numara girmesini iste en büyük olan sayıyı çıktı al.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if (num1 >= num2) and (num1 > num3):  #burada and kullanmamızın sebebi her iki koşulda true olmalı eğer bir tanesi false olursa if, elif çalışmaz.
     largest = num1                       #num1 her ikisinde büyük olması lazım ki en büyük num1 olsun.
elif (num2 >= num1) and (num2 >= num3):  #burada num2 hem num1 den hemde num3 den büyük olacak ki en büyük sayı o olsun.
     largest = num2
else:
     largest = num3
print("The largest number is", largest)

#KULLANICI BİR RAKAM GİRECEK POZİTİFSE POZİTİF, NEGATİFSE NEGATİF YAZACAK.
num = float(input("Enter a number:"))
if num > 0 :
     print("Pozitive number.")
elif num == 0 :
     print("Zero.")
else :                           #burada bir koşul yazmıyoruz yukardaki koşulların sağlamayanların tamamı burada dahil oluyor.
     print("Negative number.")

audience_group = 'kid', 'teen', 'adult'         #burada bir tuple tanımladık ve tuple içinde stringler var.
audience = "teen"

if audience in audience_group:                           #burada audience AUDİENCE GROUP ın içinde var mı yok mu diye soruyorum. Eğer audience varsa, kid mi, teen mi, adult mu?
     if audience == "kid":                             #bu if yeni bir koşul bunun altındaki elif ve else buna ait olduğu için tam onun hizasında yazıldı.
       print("it is free to go to cinema")
     elif audience == "teen":                           #bu iç kısımdaki if, elif, else bu üçü ayrı bir kod bloğu,  İLK İF İLE ELSE VE PRİNT AYRI BİR KOD BLOĞU
      print("discounted price!")
     else: #audience == "adult"
      print("normal price")
else:                                                   # bu else ilk if e ait olduğu için tam onun hizasına yazdık.
    print("No such audience, stay at your home!")              #bu print ilk if e ait yani hiçbir koşul sağlamazsa.

audience_group = 'kid', 'teen', 'adult'         
audience = "ASUMAN"                                     #BURADA AUDİENCE ASUMAN OLARAK TANIMLADIM. İÇTEKİ İF, ELİF VE ELSE Yİ SAĞLAMADIĞI İÇİN EN ALTTAKİ ELSE YE GEÇTİ

if audience in audience_group:                         
     if audience == "kid":                             
       print("it is free to go to cinema")
     elif audience == "teen":                        
      print("discounted price!")
     else: #audience == "adult"
      print("normal price")
else:                                                 
    print("No such audience, stay at your home!")

audience_group = 'kid', 'teen', 'adult'         
audiENCES = "ASUMAN"                      #BURADA AUDİENCE yerine başka bir kelime yazacağım. daha ilk if de audience AUDİENCE GROUP un içinde mi sorusunda HEMEN kod bloğu döner.

if audience in audience_group:                         
     if audience == "kid":                             
       print("it is free to go to cinema")
     elif audience == "teen":                        
      print("discounted price!")
     else: #audience == "adult"
      print("normal price")
else:                                                 
    print("No such audience, stay at your home!")

score = int (input("Enter your score :"))
if score >= 90:
  if score >= 95:
    score_letter = "A+"
  else:
      score_letter = "A"
elif score >= 80:
  if score >= 85:
    score_letter = "B+"
  else:
      score_letter = "B"
elif score >= 70:
  if score >= 75:
    score_letter = "C+"
  else:
    score_letter = "C"
else:
  score_letter = "below C"
print("Your degree: %s" % score_letter)

# KELİMELERİN CONFERTABLE OLUP OLMADIĞI İLE İLGİLİ OLARAK KÜME YARDIMIYLA KOD YAZMA
left=set("aeiufgıcvöj")   #str olan left i set e çevirdik, aynı şekilde right da.
right=set("kmlyrnhpqwsbx")
word = "clarusway"
word = set(word)

leftcheck = bool(word.intersection(left))   #word değişkenine tanımlı değerin left kümesi ile bir kesişimi varmı? varsa true döner yoksa false
rightcheck = bool(word.intersection(right))  #aynı şekilde bu kez de right kümesi ile bir kesişimi varmı ? (intersection=kesişim)
#bu left ve right AND ile bağlamamız lazım ki ikiside de true olursa sonuç confertable olsun,yani iki elinde parmakları kullanılarak yazılmış olsun.
#bir tane bile false yani boş küme çıkarsa bu şu demektir tek el ile yazılıyor, bu durumda unconfertable olur.
sonuc = leftcheck and rightcheck
sonuc   #clarusway kelimesini yazarken iki elinde parmakları kullanılır, yani hem sol hemde sağ küme ile kesişimi var.

bool(rightcheck)

#boş olan bir colletion false verir.
bool(set())

bool(set(" "))

"""# ***DÖNGÜ LER (LOOP)***"""

while 0 :                           #burada 0 false olduğu için hiç döngüye girmedi.
     print("sıfır")

while 0 :            #burada da 0 false olduğu için condition sağlanmadı ve alt satırdaki kod bloğunu verdi. sonuç true olsaydı ilk satırdakini çıkaracaktı.
    print("sıfır")
print("ali veli deli")

while 1 :            #bunu çalıştırdığım an sonsuz döngüye giriyor.
    print("sıfır")
print("asuman")

number = 0
while number < 6 :     # 0 < 6  ise kodu çalıştır, bunu iteration için yap, number += 1 dediği için.
     print(number)
     number += 1       # 6<6 gördüğü an false verir ve döngü biter. Döngüden çıktığı an alttaki kod satırını çalıştırır. BU SATIR WHİLE DÖNGÜSÜNÜN DIŞINDADIR.
print('now, number is bigger or equal to 6')  #sonsuz döngüye girmemek için sayıyı arttırarak ya da azaltarak bunu önlememiz lazım.

condition = 5
while condition :
     print(condition)   #bunu bu haliyle çıktı alırsak sonsuz döngüye girer. bu nedenle sayıyı bir şeye bağlamamız lazım, bir artma ya da azalmaya.

condition = 5               #burada sonsuz döngüyü engllemek ve döngüden çıkarmak için
while condition :
     print(condition)
     condition -= 1

condition = 5               #burada sonsuz döngüyü engllemek ve döngüden çıkarmak için
while condition :
     condition -= 1
     print(condition)

condition = 5             
while True :            #bunu yazarak yani while true dediğimiz an sonsuz döngüye girer, sonsuz döngüden çıkaran if deki koşuldur.
     condition -= 1
     print(condition)
     if condition == 0 :  # bazı şartları sağladığında döngüden çıkarmak için if kullananmak gerekir  
       break               #bu break kod kelimesi döngüden çıkarır.
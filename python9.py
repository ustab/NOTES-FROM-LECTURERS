from curses import KEY_DOWN
from pstats import SortKey
from sys import maxsize


print("DOKUZUNCU DERSTEN NOTLAR")
print()
#1. soru:numbers icerisinde en fazla tekrar etme sirasina gore 
# rakamlari siralayacagiz

numbers=[-1,3,7,4,3,0,3,16,3,7,0,0,1] #numbers.count(max(numbers))
#ilk anda dusunulen sey max ve tekrarlama(count fonksiyonu ile) sirasini hangi 
#fonksiyonlarla ortaya cikaririz olmali
print(max(numbers))
print(sorted(numbers))#kucukten buyuge siralama
print(sorted(numbers, reverse=True))#buyukten kucuge siralama
print(max(numbers, key=numbers.count))#en sik tekrar eden sayiyi bulma
#print(sorted(numbers)[-1])bununla olmuyor
#print(reversed(numbers))bunla da olmuyor
#print(sorted(numbers, key=len))#bunla calismiyor.en buyuk sayiya gore siralama

#max(numbers, key=numbers.count)
#numbers.count(max(numbers, key=numbers.count))

#2.soru: sehirlerin siralanmasi,stringlerin uzunluguna gore siralama

sehirler=["istanbul", "van", "ağri", "ankara"]
print()
print(sorted(sehirler))#harf sirasina gore siralama
print()
#print(reversed(sehirler, reverse=True))
print()
#print(reversed(sehirler, reverse=False))
#len(sehirler, key=sehirler.count)
print(sorted(sehirler,key=len))#harf sayisina gore kucukten buyuge dogru
print()
print(sorted(sehirler, key=len, reverse=True))#sorted(key: None = ..., reverse: bool = ...) ), buyukten kucuge 
#harf sayisi esas alinarak ve bool uzerinden yapilan siralama
print()
sehirler=["istanbul", "van", "ağri", "ankara"]
print()

#print(sehirler.sort(key=len)) sort methodu hocada calisti ama burda none ciktisi var
#*, key: None = ..., reverse: bool = ...) -> None
#Sort the list in ascending order and return None.

#3.soru: what is the output of this  syntax?

odd_no =[[11,[15,17],23,25,27]]
print(odd_no[0][::-1])
print()

#4.soru:
print(len([[1,2,3]][0])) #bu ciktinin sonucu soruluyor.[0]bununla distaki []kismi geciyoruz
#buna indeksleme diyoruz.




























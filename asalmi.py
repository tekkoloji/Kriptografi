# -*- coding: cp1254 -*-
import math

#ÇOMÜ Kriptografi 
#Verilen sayıyı bölecek olduğumuz sayının asal olup olmadığını kontrol eder
def bolenasalmi(x):
    sayac=0
    for i in range(1,x+1):
        if x%i==0:
            sayac=sayac+1
    if sayac==2:
        return 1
    else:
        return 0

#Öz Yinelemeli Fonksiyon
#Verilen sayının 2den kareköküne kadar olan
#asal sayılara tam bölünüp bölünmediğini kontrol eder
def asalmi(sayi,bolen):
    karekok=math.ceil(math.sqrt(sayi))
    if bolen==karekok+1:
        print "Sayı Asal"
    else:
        if bolenasalmi(bolen):
            if sayi%bolen==0:
                print "Sayı Asal değil"
            else:
                asalmi(sayi,bolen+1)
        else:
            asalmi(sayi,bolen+1)

sayi=input("Sorgulamak istediğiniz sayıyı giriniz:")
asalmi(sayi,2)







    

# -*- coding: cp1254 -*-
import math

#�OM� Kriptografi 
#Verilen say�y� b�lecek oldu�umuz say�n�n asal olup olmad���n� kontrol eder
def bolenasalmi(x):
    sayac=0
    for i in range(1,x+1):
        if x%i==0:
            sayac=sayac+1
    if sayac==2:
        return 1
    else:
        return 0

#�z Yinelemeli Fonksiyon
#Verilen say�n�n 2den karek�k�ne kadar olan
#asal say�lara tam b�l�n�p b�l�nmedi�ini kontrol eder
def asalmi(sayi,bolen):
    karekok=math.ceil(math.sqrt(sayi))
    if bolen==karekok+1:
        print "Say� Asal"
    else:
        if bolenasalmi(bolen):
            if sayi%bolen==0:
                print "Say� Asal de�il"
            else:
                asalmi(sayi,bolen+1)
        else:
            asalmi(sayi,bolen+1)

sayi=input("Sorgulamak istedi�iniz say�y� giriniz:")
asalmi(sayi,2)







    

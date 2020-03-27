# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:44:58 2020

@author: david
"""


p = 0
while p<337.25:
    kg = float(input("Ingrese el peso del paquete en kg: "))
    v = int(input("Ingrese el tipo de vuelo (nacional=1 o intercontinental=2): "))
    km = float(input("Ingrese la distancia de envío en km: "))
    if kg<10:
        print("Peso no es aceptable.")
    else:
        if v==1:
            if km>8000:
                if kg>400:
                    pf = kg*4500+km*4.971-(10*((4500*kg+4971*km)/100))
                else:
                    pf = kg*4500+km*4971
            else:
                pf = kg*4500+km*4971
        else:
            if kg<100:
                pf = kg*4500+km*4000
            else:
                pf = kg*4500+km*4.971-(15*((4500*kg+4000*km)/100))
    print("El monto que deberá pagar es: $" + str(pf))
    p=p+kg                
#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import math

def apoklisi(emb, perim, char):

    seven_perc = round(emb*0.07, 2)
    apoklisi = round((pow(math.sqrt(emb) + (2*char), 2) - emb)*(perim/(4*math.sqrt(109.3742))),2)
    
    if apoklisi > seven_perc:
        apod_apokl = seven_perc
    else:
        apod_apokl = apoklisi
    
    return apod_apokl

def main():
    emb = float(input('Εμβαδόν: '))
    perim = float(input('Περίμετρος: '))
    inp = input("a/Αστικό ή g/Αγροτικό: ")
    
    if inp == 'a':
        char = 0.5
    elif inp == 'g':
        char = 2.0
    
    print("Η αποδεκτή απόκλιση του γεωτεμαχίου είναι " + str(apoklisi(emb, perim, char)) + " τ.μ.")
    
if __name__ == "__main__":
    main()
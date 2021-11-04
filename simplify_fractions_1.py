#!/usr/bin/env python
# coding: utf-8

# In[37]:


"""The function takes numerator and denominator as inputs.
   Then returns and prints out the simplified fraction based on the greatest common divisor.
   Doesn't handle errors."""

numerator = int(input("Give me the numerator value: "))
denominator = int(input("Give me the denominator value: "))

def prog(number_up, number_down):
    for i in range(abs(number_up), 1, -1):
        if number_up % i == 0 and number_down % i == 0:
            number_up /= i
            number_down /= i

    print(str(int(number_up))+"/"+str(int(number_down)))
    print("Greatest common divisor: "+ str(int(numerator/number_up)))
    
prog(numerator, denominator)


# In[ ]:





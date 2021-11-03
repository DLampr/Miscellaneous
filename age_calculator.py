#!/usr/bin/env python
# coding: utf-8

# In[8]:


from datetime import datetime, timedelta
from dateutil import relativedelta

def age_calculator(birth_date):
    datetime_object = datetime.strptime(f'{birth_date}', '%d-%m-%Y')
    d = datetime.today()
    dx = relativedelta.relativedelta(d, datetime_object)
    
    return f'You are {dx.years} years {dx.months} months and {dx.days} days old.'

def main():
    age = input(f'Insert Your Birth Date (dd-mm-YYYY):\n')
    print(age_calculator(age))

if __name__ == "__main__":
    main()


# In[ ]:





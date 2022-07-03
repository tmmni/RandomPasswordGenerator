#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random
import string


# In[44]:


while True:
    x = int(input("Enter the number of characters for generating your password - "))
    if x in range(8):
        print("Please enter 8 or more characters!")
        continue
    elif x in range(8,11):
        n = 2
        break
    elif x in range(11,14):
        n=3
        break
    elif x in range(14,17):
        n=4
        break
    else:
        print('Number of characters is out of range!')
spec = [random.choice(string.punctuation) for i in range(n)]
num = [random.choice(string.digits) for i in range(n)]
cap = [random.choice(string.ascii_uppercase) for i in range(n)]
low = [random.choice(string.ascii_lowercase) for i in range(x-(3*n))]
password = spec+num+cap+low
random.shuffle(password)
password = ''.join(password)
print(f'Your randomly generated password is {password}')


# In[ ]:





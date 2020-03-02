#!/usr/bin/env python
# coding: utf-8

# In[2]:


def BODMAS():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print("Enter the desired operation you like to perform")
    symbol = input("Enter one of these symbols for an operation +,-,*,/: ")
    
    result = ()

    if symbol == '+':
        result = num1 + num2

    elif symbol == '-':
        result == num1 - num2

    elif symbol == '*':
        result = num1 * num2

    elif symbol == '/':
        result = num1 / num2

    else:
        print("cant recognize this input. try again ")

    print(num1, symbol, num2, ":", result)


# In[ ]:





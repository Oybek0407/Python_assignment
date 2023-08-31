#!/usr/bin/env python
# coding: utf-8

# In[26]:


# a- print first 10 integers and their squares
a=0
while a<11:
    a+=1
    print(a, "=>" ,a**2)


# In[ ]:





# In[25]:


# b- print the first 10 natural numbers in reverse order 
a=11
while a>=1:
    a-=1
    print(a)


# In[ ]:





# In[24]:


# c- compute the sum of numbers until a user types zero
sum=0
while True:
    num=int(input("input a number or for stoping 0 : "))
    if num==0:
        break
    sum+=num
print(f" sum of numbers: {sum}")


# In[ ]:





# In[ ]:


# d- compute several inputs from a user and display the largest and smallest values
input_number=int(input("How many numbers do u want enter? "))
count=0
num=[]
while count<input_number:
    number=float(input("Enter number: ")) 
    num.append(number)
    max_num=max(num)
    min_num=min(num)
    count+=1
    
print(f'smallest :{min_num}')
print(f"largest : {max_num}")


# In[35]:


import statistics as st


# In[43]:


# e- compute several inputs from a user and display the mean value of the
#.  inputted values.
input_number=int(input("How many numbers do u want enter? "))
count=0
num=[]
while count<input_number:
    number=float(input("Enter number: ")) 
    num.append(number)
    mean_num=st.mean(num)
    count+=1
    
print(f"Mean of numbers is :{mean_num}")


# In[ ]:





# # for loop

# In[54]:


# a - display numbers from -10 to -1 
for x in range(-10, 0):
    print(x)


# In[85]:


# b-  accept a number from a user and calculate the sum of all numbers from 1 to a given number;
number=int(input("Enter a number :"))
sum_num=0
for x in range(1, number+1):
    sum_num+=x
print(f"sum of number is :{sum_num}")   


# In[3]:


# c-  print all prime numbers between 50 and 100
for x in range(50, 100+1):
    for y in range(2, x):
        if x%y==0:
            break
    else:
        print(x)   


# In[ ]:


# d- print the first 15 Fibonacci sequence
f_n=[0,1]
for x in range(2, 15):
    z=f_n[x-1]+f_n[x-2]
    f_n.append(z)
print(f_n)
    


# In[19]:


# e- computes the factorial of 7
total=1
n=7
for x in range(1, n+1):
    total=total*(x)
print(total)


# # list/ Dictionary

# In[31]:


# a- create a list from elements of a range from 10 to 50 with a step of 5 using
##  list comprehension;
b=list(range(10, 51, 5))
print(b)


# In[33]:


# b-create a list that contains squares of the list from 4.a
for a in b:
    squared=a**2
    print(squared)


# In[39]:


# c- create a list that contains elements greater than 100 of the list from 4.b
for a in b:
    if a**2>100:
        squared=a**2
        print(squared)


# In[103]:


# d- creat two list of name of vehicles with their wieght one of them below 5000 and larger than 2000 
list_5000=[]
list_2000=[]
di = {"Sedan": 1500, 
      "SUV": 2000, 
      "Pickup": 2500, 
      "Minivan": 1600, 
      "Van": 2400, 
      "Semi": 13600, 
      "Bicycle": 7, 
      "Motorcycle": 110}
for item in di:
    if di[item]<5000:
        list_5000.append(item)
    if di[item]>2000:
        list_2000.append(item)
print(list_5000)
print(list_2000)


# In[107]:


list_2000=[item.upper() for item in di if di[item]>2000]
list_5000=[item.upper() for item in di if di[item]< 5000]
print(list_5000)
print(list_2000)


# In[ ]:





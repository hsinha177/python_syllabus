# -*- coding: utf-8 -*-

#Program to compute fibonacci series less than 4 million and print sum of all the even terms

f=0                                                     #first number
s=1                                                     #second number
fl=[0,1]                                                #list for fibonacci series
t=0                                                     #third number in series
even=0                                                  #sum of even term variable
num = int(input("Enter the series frequency : "))       #loop for series
for i in range(2,num):
    t=f+s                                               #finding next term in series
    if t<4000000:                                       #for numbers less than 4 million
        f=s
        s=t
        fl.append(t)
        if t%2 == 0:                                    #even term checks & sum
            even+=t
    else:
        break
#printing results
print("Fibonacci Series of "+str(num)+" term less than 4 millions are : ")
print("\n")
print(fl)
print("\n")
print("Sum of all even term : "+str(even))
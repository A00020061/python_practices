# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:49:27 2021

@author: sande
"""
#sending email
# =============================================================================
# import getpass
# import smtplib
# smtp_object = smtplib.SMTP('smtp.gmail.com',587)
# (smtp_object.ehlo())
# (smtp_object.starttls())
# password=getpass.getpass('pasword please: ')
# email=getpass.getpass('gmail please: ')
# password=getpass.getpass('pasword please: ')
# (smtp_object.login(email,password))
# 
# from_address=email
# to_address=email
# subject=input('enter the subject line:')
# message=input('enter the body message')
# msg='subject: '+subject+'/n'+message   
# (smtp_object.sendmail(from_address, to_address, msg))
# print(smtp_object.quit())
# =============================================================================
# =============================================================================
# import imaplib
# m=imaplib.IMAP4_SSL('imap.gmail.com')
# import getpass
# email=getpass.getpass('email here: ')
# password=getpass.getpass('password here: ')
# m.login(email,password)
# (m.list())
# m.select('inbox')
# typ, data=m.search(None,'since "10-Aug-2021"')
# email_id=data[0]
# 
# result, email_data=m.fetch(email_id, '(RFC822)')
# raw_email=email_data[0][1]
# raw_email_string=raw_email.decode('utf-8')
# import email
# email_message=email.message_from_string(raw_email_string)
# for part in email_message.walk():
#     if part.get_content_type()=='text/plain':
#         body=part.get_payload(decode=True)
#         print(body)
#         
# =============================================================================
# =============================================================================
# 
# n=5
# print(*range(1,n+1),sep='')
# print(*'hello')
# =============================================================================
# # =============================================================================
# import re
# 
# text='how are you bro today i sumbitted my third internship application at royal automobile association and i hope i wll definitely get this opportunity and start my career in this field'
# # =============================================================================
# # a=re.findall('\\bt\w+\\b',text)
# # b=re.findall('today',text)
# # c=re.findall(r'^\w+',text)
# # d=re.split(r'\s', text)
# # e=map(lambda x:x.text(),re.finditer(r'\w',text))
# # print(e)
# # =============================================================================
# # =============================================================================
# # print(text.split(','))
# # print(c)
# # 
# # print(b)
# # print(a)
# # print(d)
# 
# a=re.findall()
# =============================================================================
'''
x=[1,2,3]
y=[4,5,6]
result=[]
for i in (x):
    for j in y:
        
        result.append([i,j])
print(result)

x=[1,2,3]
y=[4,5,6]
print([[i,j] for i in x for j in y])
print([z for z in range(10)])
print([a for a in range(16) if a%3==0])
'''
#print([[x,y,z] for x in range(2) for y in range(2) for z in range(2) if (x+y+z)!=2])
# =============================================================================
# from collections import defaultdict
# 
# def check(n,arr):
#     d=defaultdict(int)
#     for i in arr:
#         d[i]+=1
#         print(d)
#     cnt=0
#     for ele in d.values():
#         cnt+=ele//2
#         print(cnt)
#     return cnt
# arr=[11,12,13,14,11,15,13,14]
# n=8
# res=check(n,arr)
# print(res)
# 
# =============================================================================
# =============================================================================
# 
# a={"brand": "Ford",
#   "model": "Mustang",
#   "year": 1964}
# print(a.values())
# a['year']=2018
# for i in a.values():
#     print(i)
# =============================================================================
'''
#here i add the two arrays and convert into singel list that has the sum of both arrays
n=int(input('what='))
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
total=[]

for i in range(0,n):
    total.append((num1[i]+num2[i]))
print(total)
for i in total:
    print(i,end=' ')
#print('')

from collections import Counter
customer=2
shoes=10
number=Counter([2,3,4,5,6,8,7,6,5,18])
income=0

for i in range(customer):
    size,price=map(int,input().split())
    if number[size]:
        income+=price
        number[size]-=1
        
#print(income)
'''
arr={'january':2200,'february':2350,'march':2000,'april':2130,'may':2190}
a=list(arr.values())
#print('how many dollar spent', (a[1]-a[0]))
total=0
for i in range(0,len(a)-2):
    total +=a[i]
#print(total)
'''
#if 2000 in a:
    print(True)
    
else:
    print(False)'''
arr['june']=1980
arr.update({'april':1930})
print(arr)


    



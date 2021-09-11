# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:42:34 2021

@author: sande
"""
# =============================================================================
# 
# import random
# 
# attempt_score=[]
# def show_score():
#     if len(attempt_score)<=0 
#         print('you do not hava a score yet, please try again! ')
#     else:
#         print('you attempting score is {} in game'.format(min(attemp_score)))
# def start_game():
#     computer=int(random.randint(1,10))
#     player_name=input('what is your name= ')
#     guess=int(input('what is your gusessing about between 1 to 10'))
#     wanna_play=input('hi {}, do you want you play this game (Enter Yes/No) '.format(player_name))
# while wanna_play.lower()=='Yes':
#     try:
#         
#     attempt=0
#     show_score()
#     if   0<=guess>10:
#         raise ValueError('please select given range number ! ')
#         if guess==computer:
#             print('nice! you got a right number ')
#             print('you got a right number with {} attempt'.format(attempt))
#             attempt +=1
#             attempt_score.append(attempt)
#             play_again=input('you want to play again (Enter Yes/no)')
#             attempt=0
#             show_score()
#             computer=int(random.randint(1,10))
#             if play_again=="No":
#                 print('thanks! hope you have a good day')
#                 break
#      elif guess<computer:
#          print('you got a low value! ')
#          attempt +=1
#          
#      elif guess>computer:
#          print('you have a high value')
#          attemtp +=1
#     except valueerror as err:
#         print('oh no! this is not a valid value')
#         print('{}'.format(err))
# else:
#     print('that is cool, have a good day')
#     
# 
# if __name=='__main__':
#     start_game()
# 
#     
# 
# =============================================================================

# =============================================================================
# def addition ():
#     print("Addition")
#     n = float(input("Enter the number: "))
#     t = 0 #//Total number enter
#     ans = 0
#     while n != 0:
#         ans = ans + n
#         t+=1
#         n = float(input("Enter another number (0 to calculate): "))
#         return [ans,t]
# print(addition())
# 
# =============================================================================
# =============================================================================
# 
# class book():
#     def __init__(self,title,author,year,pages):
#         self.title=title
#         self.author=author
#         self.year=year
#         self.pages=pages
#     def __str__(self):
#         return f'{self.title} by {self.author} is the writer'
#     def __len__(self):
#         return self.pages
#     def __add__(self,company):
#         self.company=company
#     
# 
# b=book('pythonscore', 'ankit sharma','2009',200,'hello')
# 
# print(b.company)
# print(b)
# a=len(b)
# print(a)
# =============================================================================
# =============================================================================
# class Bank():
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     
#     def deposit(self,dep):
#         
#         self.balance=self.balance+dep
#         
#         
#         return (self.balance)
#     
#     def withdraw(self):
#          a=int(input('how much money you want to withdraw='))
#          if self.balance>=a:
#              fund=(self.balance-1.50) -a
#              return fund
#          else:
#              print('fund unavailable')
#              print('thanks ')
#     def __str__(self):
#         return f'owner {self.name} \nbalance {self.balance}'
# dep=int(input('how much money you want to deposit='))
#      
# h=Bank('ankit',1000)
# print(h)
# print(h.deposit(dep))
# print(h.withdraw())
# =============================================================================
# 
# def main(text):
#     wordlist=text.split()
#     revese_list=wordlist[::-1]
#     return '+'.join(revese_list)
# a=main('who are you')
# print(a)
#     
# =============================================================================

# =============================================================================
# 
# def game():
#     i=1
#     sandy='wrong'
#     andy='wrong'
#     while sandy and andy=='wrong':
#         try:
#             sandy=int(input('guess the number(0,100): '))
#             andy=int(input('guess the number(0,100): '))
#         except:
#             print('sorry! you choose a wrong number: try agian= ')
#             continue
#         if i<6:
#             
#             sandy=int(input('guess the number(0,100): '))
#             andy=int(input('guess the number(0,100): '))
#             if sandy<andy:
#                 print(f'{sandy}! your number is lessthan to {andy} numebr!')
#                 print(f'now! {sandy} you have a {6-i} attempt: ')
#                 i +=1
#             elif sandy>andy:
#                 print(f'{sandy}! your number is greater than {andy}: ')
#                 print(f'now! you have a {6-i} attempt! ')
#                 i +=1
#             elif sandy==andy:
#                 print(f'you both have a same gueesed numebr! ')
#                 i+=1
#             else:
#                 print('no one is winnner for this game: ')
#                 break
# def main():
#     game()
#     ask=input('want to play again(y/n)! ')
#     if ask =='y':
#         game()
#     else:
#         print('thanks for playing game!')
# main()
# =============================================================================
# =============================================================================
# 
# def song(bottles):
#     #bottles=99
#     while True:
#         
#         for i in range(1,bottles+1):
#             if i>0:
#                 
#                 print(f'{bottles} bottles of beer on the wall,{bottles} bottles of beer.')
#                 print(f'Take one down and pass it around, {bottles-1} of beer on the wall.')
#                 i+=1
#                 bottles-=1
#                 
#             elif i==0:
#                 print('how are you bro! ')
#             break
# 
# 
# a=song(15)  
# print(a)     
# =============================================================================
# =============================================================================
# 
# def song(n):
#     while True:
#         for i in range(1,n+1):
#             if n==1:
#                 object='bottle'
#                 objects='bottles'
#                 print(f'{n} {object} of the beer on the wall, {n} {object} of beer.')
#                 print(f'Take one down and pass it around,0 {object} of beer on the wall.')
#             break
#             elif n==2:
#                 object='bottles'
#                 objects='bottle'
#                 print(f'{n} {objects} of beer on the wall, {n} {object} of beer.')
#                 print(f'Take one down and pass it around, {n} {objects} of beer on the wall.')
#                 n-=1
#                 i+=1
#              break
#             else:
#                 print(f'{n} bottles of beer on the wall, {n} bottles of beer.')
#                 print(f'Take one down and pass it around, {n} bottles of beer on the wall.')
#                 n-=1
#                 i+=1
#             break
#                 
# a=song(50)
# print(a)
# =============================================================================
# =============================================================================
# import random
# answer=['it is certain','it is decidely so',' without a doubt', 'donot worry', 'yes-definitely','you may rely on it']
# print('  __  __          _____ _____ _____    ___  ')
# print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
# print(' | \  / |  /  \ | |  __  | || |      | (_) |')
# print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
# print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
# print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
# 
# print('hello world, i am the magic 8 ball, what is your name? ')
# name=input()
# print('hello' +name)
# 
# def magic8ball():
#     print('ask me a question')
#     input()
#     #print(answer[random.randint(0,len(answer)-1)])
#     print(random.randint(answer))
#     print('i hope that helped')
#     replay()
# def replay():
#     print('do you have another question?(y/n):')
#     reply=input()
#     if reply=='y':
#         magic8ball()
#    
#     else:
#         print('i apologies, i did not catch that. please repeat.')
#         
#         
# magic8ball()
#     
# =============================================================================
# =============================================================================
# import random
# 
# fname=['sandeep','ankit','rahul','karan','ankur']
# lname=['kumar','singla','singh','chand','sain']
# street=['shartri','maple','magrate','hampstaded','regency']
# state=['haryana','punjab','himachal','jammu','rajasthan']
# country=['india','pakistan','srilanka','nepal','bangladash']
# 
# class Person():
#     def __init__(self,num=3):
#         self.num=num
#     @property
#     def first_name(self):
#         for i in range(self.num):
#             first=random.choice(fname)
#             print (first)
#     @property       
#     def last_name(self):
#         for i in range(self.num):
#             last=random.choice(lname)
#             print(last)
#     @property        
#     def full_name(self):
#         for i in range(self.num):
#             first=random.choice(fname)
#             last=random.choice(lname)
#             print(f'{first} {last}')
#             
#     def mobile(self):
#         return (f'+91-{random.randint(800,999)}{random.randint(800,999)}{random.randint(800,999)}{random.randint(1000,9999)}')
#             
#    
#         
#             
#             
# 
# details=Person(3)
# print(details.first_name)
# print(details.full_name)
# print(details.mobile())
#        
# 
# =============================================================================
# =============================================================================
# 
# import bs4
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen
# 
# news_url="https://news.google.com/news/rss"
# Client=urlopen(news_url)
# xml_page=Client.read()
# Client.close()
# 
# soup_page=soup(xml_page,"xml")
# news_list=soup_page.findAll("item")
# # Print news title, url and publish date
# for news in news_list:
#   print(news.title.text)
#   #print(news.link.text)
#   #print(news.pubDate.text)
#   print("-"*60)
#     
# =============================================================================
# =============================================================================
# import bs4
# from urllib.request import urlopen
# from bs4 import Beautifulsoup as soup
# news_url='https://www.indiatoday.in/aajtak-livetv'
# ankit=urlopen(news_url)
# xml_page=ankit.read()
# ankit.close()
# 
# soup_page=soup(xml_page,'xml')
# news_list=soup_page.findall('item')
# for news in news_list:
#     print(news.title.text)
# =============================================================================
# =============================================================================
# 
# import requests
# api_key='54ae4300fd07413799d9192b58a159f1'
# 
# def news():
#     news_url='https://news.google.com/topstories?hl=en-AU&gl=AU&ceid=AU:en'
#     news_=requests.get(news_url).json()
#     article=news_['articles']
#     
#     news_article=[]
#     for arti in article:
#         news_article.append(arti['title'])
#         
#     for i in range(10):
#         print(i+1, news_article[i])
#         
#         
#         
#         
#         
#     
#         #print(news_article)
# result=news()
# print(result)
# =============================================================================
# =============================================================================
# def leap_year(n):
#     if n%400==0:
#         print(f'it is a {n}leap year')
#     elif n%100==0:
#         print(f'this is not {n} leap year')
#     elif n%4==0:
#         print(f'this is  {n} a leap year')
#     else:
#         print('not a leap year')
# n=int(input('what is the year'))        
# leap_year(n)
# =============================================================================
# =============================================================================
# 
# from datetime import date,timedelta
# a=(date.today())
# difference=a-timedelta(202)
# print(difference)
# ==========================================================================0===
# =============================================================================
# =============================================================================
# # 
# from datetime import date
# from datetime import datetime
# import time
# =============================================================================

# =============================================================================
# timee=datetime.datetime.strptime('Jul 2 2014 2:43pm', '%b %d %Y %I:%M%p')
# timm=datetime.datetime.now().time()
# print(timee)
# print(timm)
# =============================================================================
# =============================================================================
# 
# datee=date.today()
# df=datetime.timedelta(5)
# a=datee-df
# print(a)
# =============================================================================
# =============================================================================
# def days():
#     today=date.today()
#     yesterday=today-(datetime.timedelta(1))
#     tomorrow=today+(datetime.timedelta(1))
#     print('today',today)
#     print(yesterday)
#     print(tomorrow)
# days()
# 
# =============================================================================

#print(datetime.combine(date.today(), datetime.min.time()))

import csv
# this is the way of reading the csv file and all the information will be displayed infront of you.

# =============================================================================
# with open('csvfile.csv',mode='r') as file:
#     what=csv.reader(file)
#     for lines in file:
#         print(lines)
# =============================================================================
# now i going to write a code that write a csv file and make some changes that required for that. good luck guys
# =============================================================================
# fields=['game','age','salary']
# rows=[['cricket','26','$15000'],
#       ['footbal','28','$16000'],
#       ['badminton','30','$18000']]
# 
# filename='universityfile.csv'
# with open('universityfile.csv',mode='w') as csvfiles:
#     whats=csv.writer(csvfiles)
#     print(whats.writerow(fields))
#     print(whats.writerows(rows))
#     print(whats)
# =============================================================================
# =============================================================================
# 
# with open('csvfile.csv',mode='r') as file:
#      what=csv.DictReader(file)
#      print('gmail')
#      print('----------------------')
#      for lines in what:
#          print(lines['email'])
# 
# =============================================================================
# =============================================================================
# fields=[]
# rows=[]
# with open('csvfile.csv', newline='') as  csvfiles:
#     what=csv.reader(csvfiles)
#     fields=next(what)
#     for row in what:
#         print(','.join(row))
# print(what.line_num )
# print(','.join(field for field in fields))
# =============================================================================
# =============================================================================
# import csv
# import sys
# with open('csvfile.csv', 'wt') as f:
#     writer = csv.writer(f)
#     writer.writerow(('id1', 'id2', 'date'))
#     for i in range(3):
#         row = (
#             i + 1,
#             chr(ord('a') + i),
#             '01/{:02d}/2019'.format(i + 1),)
#         writer.writerow(row)
#         print(i)
# print(open('csvfile.csv', 'rt').read())
# 
# =============================================================================
# =============================================================================
# data=[[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
# with open('csvfile.csv', 'w') as files:
#     what=csv.writer(files)
#     what.writerows(data)
# with open('csvfile.csv') as file:
#     data=csv.reader(file)
#     for row in data:
#         print(row)
# =============================================================================
'''
print(bin(1024))
print(hex(1024))
print(round(5.23222,2))
'''
# =============================================================================
# s='hello how are you Mary, are you feeling okay?'
# print(s.lower())
# s1='twywywtwywbwhsjhwuwshshwuwwwjdjdid'
# print(s1.count('w'))
# 
# s={2,3,1,5,6,8}
# s1={3,1,7,5,6,8}
# print(s.union(s1))
# print({k:k**3 for k in range(5)})
# list1=[1,2,3,4,5,7,8,9,65,5,6,7,8,9]
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)
# =============================================================================
# 
# from ipywidgets import interact,interactive,fixed
# import ipywidgets as widgets
# def func(x):
#     return x
# a=func(10)
# print(a)
# print(interact(func,x=10))
# =============================================================================
a=[1,5,6,9,8,45]
print(list(m



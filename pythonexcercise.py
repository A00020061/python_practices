# =============================================================================
# sum=lambda a: a+20
# multi= lambda x,y: x*y
# print(sum(20))
# print(multi(10,20))
# =============================================================================
# import random
# x=random.randint(0,10)
# a=lambda q:q*x
# print(a(10))
# =============================================================================

# =============================================================================
# msg=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# msg.sort(key=lambda x:x[1])
# =============================================================================
#import pdb
# =============================================================================
# msg=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'alue'}]
# #pdb.set_trace()
# msg1=sorted(msg,key=lambda x:x['make'])
# msg.sort()
# print(msg1)
# =============================================================================
# =============================================================================
# 
# num=[1,2,5,6,9,3,4,7,8,5,2,3,6,9,4,7,5,6]
# print(list(map(lambda x:x**2,num)))
# print(list(map(lambda x:x**3,num)))
# =============================================================================

# =============================================================================
# check=lambda x: True if x.startswith('p') else False
# print(check('lython'))
# =============================================================================
# import datetime
# check=datetime.datetime.today()
# year=lambda x:x.year
# time=lambda x:x.time()
# print(check)
# print(year(check))
# print(time(check))


# =============================================================================
# ask='45'
# #check=lambda x:True if x
# score=lambda x:x.replace('.','',1).isdigit()
# print(score('45.695')) 
# scoree=lambda a:score(a[1:]) if a[0]=='-' else score(a)
# print(scoree('-45.56'))

# =============================================================================
# def fba(n):
#     a=0
#     b=1
#     count=0
#     while count<=n:
#         print(a)
#         z=a+b
#         a=b
#         b=z
#         count +=1
#         
# result=fba(6)
# print(result)
#from functools import reduce
# =============================================================================
# a1=[1, 2, 3, 5, 7, 8, 9, 10]
# a2=[1, 2, 4, 8, 9]
# #a3=set[a1+a2]
# check=list(filter(lambda x:x in a1,a2))
# #check1=list(map(lambda x: x in (a1,a2),a3))
# print(check)
# =============================================================================

msg=[1, 2, 3, 5, 7, 8, 9, 10]
check=len(list(filter(lambda x: (x%2==0),msg)))
    
print(check)

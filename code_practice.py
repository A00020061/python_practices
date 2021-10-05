# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:06:50 2021

@author: sande
"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end=' ')
            temp=temp.next
            
    def prepend(self,value):
        node=Node(value)
        if self.length==0:
            self.head=node
            self.tail=node
            
        else:
            node.next=self.head
            self.head=node
        self.length +=1
        return True
    def append(self,value):
        node=Node(value)
        if self.length==0:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.length +=1
        return True
    
    def insert(self,index,value):
        node=Node(value)
        if index<0 or index>self.length:
            return False
        temp=self.head
        pre=self.head
        if index==0:
            node.next=self.head
            self.head=node
        if index==self.length:
            self.tail.next=node
            self.tail=node
        for _ in range(index-1):
            pre=temp
            temp=temp.next
        node.next=temp.next
        temp.next=node
        self.length+=1
        return True
    def get(self,index):
        if index<0 or index>self.length:
            return False
        temp=self.head
        
        if index==0:
            return temp.value
        for _ in range(index):
            pre=temp
            temp=temp.next
        return temp.value
    def set(self,index,value):
        if index<0 or index>self.length:
            return False
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
        return True
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
    def pre_pop(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length -=1
        if self.length==0:
            self.tail=None
        return temp.value
    
    
    def remove(self,index):
        if index<0 or index>self.length:
            return False
        temp=self.head
        pre=self.head
        if index==0:
            self.head=self.head.next
            temp.next=None
        if index==self.length:
            for _ in range(index):
                pre=temp
                temp=temp.next
            self.tail=pre
            temp.next=None
        for _ in range(index):
            pre=temp
            temp=temp.next
        pre.next=temp.next
        temp.next=None
        self.length -=1
        return temp.value
            
    
            
            
        
        
        
    
    

my=LinkedList()
my.prepend(4)
my.prepend(5)
my.prepend(6)
my.prepend(7)
my.append(2)
my.insert(4,3)
my.insert(2,10)
my.set(2,20)
#print(my.pop())

#print(my.get(0))
#print(my.pre_pop())
print(my.remove(6))
print(my.remove(2))
print(my.remove(0))


my.print_list()
    
#In this code i will run few commands in which how i can remove node (first, last and in mid of the linkedlist)
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Linkedlist:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
            
    def append(self,value):
        node=Node(value)
        if self.length==0:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.length +=1
        
    def insert(self,value):
        node=Node(value)
        if self.length==0:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
        self.length +=1
        
    def delatenode(self,value):
        temp=self.head
        pre=self.head
        while temp.next:
            if temp is not None and temp.value==value:
                self.head=self.head.next
                temp.next=None
                self.length-=1
                return temp.value
            if temp.value!=value:
                pre=temp
                temp=temp.next
            if temp.next is None and temp.value!=value:
                print('value doesnot exist')
            elif temp.next is None and temp.value==value:
                pre.next=None
            elif temp.next is not None and temp.value==value:
                pre.next=temp.next
                temp.next=None
                self.length-=1
                return temp.value
           
                
        
                
        
my=Linkedlist(40)
my.append(25)
my.append(64)
my.insert(23)
my.insert(29)
my.delatenode(29)
my.delatenode(25)
my.print_list()

        

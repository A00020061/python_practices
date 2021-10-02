# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:07:51 2021

@author: sande
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Queue:
    def __init__(self,value):
        node=Node(value)
        self.first=node
        self.last=node
        self.length=1
        
    def inqueue(self,value):
        node=Node(value)
        if self.length==0:
            self.first=node
            self.last=node
        else:
            self.last.next=node
            self.last=node
        self.length+=1
        
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length -=1
        return temp.value
    
    def print_list(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
            
            
            
my=Queue(1)
my.inqueue(2)
my.inqueue(3)
my.dequeue()


my.print_list()
        
        
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:35:01 2021

@author: sande
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self,value):
        node=Node(value)
        self.top=node
        self.height =1
        
    def prepend(self,value):
        node=Node(value)
        if self.height==0:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.height+=1
        
        
    def pop(self):
        if self.height==0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height -=1
        return temp
            
            
        
    def print_list(self):
        temp=self.top
        while temp:
            print(temp.value)
            temp=temp.next
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
my=Stack(4)
my.prepend(5)
my.prepend(6)
my.pop()
my.print_list()
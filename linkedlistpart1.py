# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 00:41:45 2021

@author: sande
"""


#there are few data structure and algorithm that we need to apply in the code for making it fast and less time consuming and memory.
# it is only possible by using proper and exact data structure and algorithm for the code or the problem

#tthere are few data structure and algorithm that we need to apply in the code for making it fast and less time consuming and memory.
# it is only possible by using proper and exact data structure and algorithm for the code or the problem
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
        
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
        self.length -=1
        # if we got a length 0 after walk through the while loop
        # we need to stop the process by adding some code lines like this one below
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value #we can add value like return temp.value for getting the full 
    #information about the linkedlist and get better understanding of the code
    def prepend(self,value):
        #this is a prepend method in which given value will be added starting of the list and 
        #head will replace the position with new given value.
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1
        return True
    # pop first element form the list 
    def pop_first(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length -=1
        if self.length==0:
            self.tail=None
        return temp.value #if you add value in temp.value will show you return value that pop up
    
    def get(self, index):
        if index< or index>self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set(self,index,value):
        if index< or index>self.length:
            return None
        temp=self.head
        for _in range(index):
            temp=temp.next
        if temp:
            temp.value=Value
        return temp


my_list=LinkedList(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.prepend(10)
my_list.pop_first()
my_list.pop_first()
my_list.pop_first()
print(my_list.print_list())

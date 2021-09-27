# this is the second way of linkedlist where every number/elements shows the both directions conductor
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class Doublelinkedlist:
    def __init__(self.value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
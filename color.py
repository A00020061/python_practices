class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
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
    
    def remove(self,index):
        if index<0 or index>self.length:
            return None
        temp=self.head
        
        if index==0:
            self.head=self.head.next
            temp.next=None
        if index==self.length-1:
            while temp.next:
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
        for _ in range(index):
            pre=temp
            temp=temp.next
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp        





        
            




my=Linkedlist()
my.prepend(10)
my.prepend(20)
my.prepend(30)
my.prepend(40)
my.remove(0)

my.print_list()

        
>>>>>>> sandy4405-patch-2

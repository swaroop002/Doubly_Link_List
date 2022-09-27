class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_data_from_tail(self,data):
        self.node=Node(data)
        if self.head==None and self.tail==None:
            self.head=self.node
            self.tail=self.node
            print("Node added")
        else:
            self.tail.next=self.node
            self.node.prev=self.tail
            self.tail=self.node
            print("Node added")

    def add_data_from_head(self,data):
        self.node=Node(data)
        if self.head==None and self.tail==None:
            self.head=self.node
            self.tail=self.node
            print("Node added")
        else:
            self.head.prev=self.node
            self.node.next=self.head
            self.head=self.node
            print("Node added")
    def add_data_after(self,prev,node):
        self.node=Node(data)
        self.counter=self.head
        while self.counter.data!=prev:
            self.counter=self.counter.next
        self.node.prev=self.counter
        self.node.next=self.counter.next
        self.counter.next.prev=self.node
        self.counter.next=self.node
        
    def remove_data_from_tail(self):
        if self.head==None and self.tail==None:
            print("Can't Remove")
        else:
            self.counter=self.head
            while self.counter.next!=None:
                self.counter=self.counter.next
            self.tail=self.counter.prev
            self.counter.prev.next=None
            print("Node Deleted")
    def remove_data_from_head(self):
        if self.head==None and self.tail==None:
            print("Can't Remove")
        else:
            self.head.next.prev=None
            self.head=self.head.next
            print("Node Deleted")
    def search(self,data):
        if self.head==None and self.tail==None:
            print("List Empty")
        else:
            count=0
            flag=0
            self.counter=self.head
            while self.counter.next!=None:
                if self.counter.data==data:
                    flag=1
                    break
                else:
                    count+=1
                    self.counter=self.counter.next
            if(flag==0):
                print("Element Not Present")
            else:
                print("Element Present at ",count)
    def display(self):  
        if self.head==None and self.tail==None:
             print("empty")
        else:
            self.counter=self.head
            while self.counter.next!=None:
                print(self.counter.data)
                self.counter=self.counter.next
            print(self.tail.data)
l1=LL()
print('Enter option tht you want to perform') 
op=int(input('1:Insert At End \n2 : Insert At Beginning \n3 : Insert After\n4 : Remove Name from End\n5 : Remove Name from Beginning\n6 : Search For Name\n7 : Display List\n')) 
while(op<=8):
    if(op==1):
        data=(input('Enter name to add : ')) 
        l1.add_data_from_tail(data) 
    elif(op==2): 
        data=(input('Enter name to add : ')) 
        l1.add_data_from_head(data)
    elif(op==3): 
        prev=(input('Enter Previous : ')) 
        data=(input('\nEnter name to add : '))
        l1.add_data_after(prev,data)
    elif(op==4): 
        l1.remove_data_from_tail()
    elif(op==5): 
        l1.remove_data_from_head()
    elif(op==6):
        data=(input('Enter name to Search : ')) 
        l1.search(data)
    elif(op==7): 
        l1.display()
    else: 
        print("Invalid option.")
    op=int(input('1:Insert At End \n2 : Insert At Beginning \n3 : Insert After\n4 : Remove Name from End\n5 : Remove Name from Beginning\n6 : Search For Name\n7 : Display List\n'))  
print("Enter option that you want to perform") 
op=int(input('1:Insert At End \n2 : Insert At Beginning \n3 : Insert After\n4 : Remove Name from End\n5 : Remove Name from Beginning\n6 : Search For Name\n7 : Display List\n')) 

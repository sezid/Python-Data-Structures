class Node:
    def __init__(self,e,n,p):
        self.element=e
        self.prev=p
        self.next=n

class DoublyList:
    def __init__(self,a):
        self.head=Node(None,None,None)#dummy
        self.head.next=self.head
        self.head.prev=self.head
        
        
        if len(a)!=0:
            i=0
            while i<len(a):
                new_node=Node(a[i],None,None)
                last_n=self.head.prev
                new_node.next=self.head
                self.head.prev=new_node
                last_n.next=new_node
                new_node.prev=last_n
                i=i+1
            
          

    def showList(self):
        n=self.head.next
        if self.head.next==self.head:
            print('List is empty')
            return None

        while n is not self.head:
            print(n.element)
            n=n.next
    def insert_tail(self,element):
        new_node=Node(element,None,None)
        n=self.head.next
        while n is not self.head:#check value exists
            if element==n:
                return 'Element already exists'
            n=n.next  
        tail=self.head.prev
        self.head.prev=new_node
        new_node.next=self.head
        tail.next=new_node
        new_node.prev=tail
    def getCount(self):#find lenght of DHDLCL
      c=0
      n=self.head.next
      while n is not self.head:
        c=c+1
        n=n.next
      return c  

    def NodeAt(self,idx):
      i=0
      n=self.head.next
      while n is not self.head:
        if idx==i:
          return n
        n=n.next
        i=i+1  


    def insert(self,element,idx):
      
        n=self.head.next
        i=0
        while n is not self.head:#check value exists
            if element==n:
                return 'Element already exists'
            n=n.next 
        n=self.head.next  
        if idx<0 and idx>=self.getCount():
            return 'Invalid index'
        else:
            if idx==0:
                new_node=Node(element,None,None)
                prev_head=self.head
                new_node.prev=self.head.prev
                self.head.prev.next=new_node
                prev_head.prev=new_node
                new_node.next=prev_head
                return self.head
            else:
                while n is not self.head:
                    if i==idx:
                        pred=self.NodeAt(idx-1)
                        successor=pred.next
                        x=Node(element,successor,pred)
                        pred.next=x
                        x.prev=pred
                        x.next=successor
                        successor.prev=x
                    i=i+1
                    n=n.next 
    def remove(self,idx):
        n=self.head.next
        i=0
        if idx<0 and idx>=self.getCount():
            return 'Invalid index'
        else:
            if idx==0:
                new_head=self.head.next
                new_head.prev=self.head.prev
                self.head.prev.next=new_head
                self.head.prev=None
                self.head.next=None
                self.head=new_head
          
            while n is not self.head:
                if i==idx:
                    pred=self.NodeAt(i-1)
                    d_node=self.NodeAt(i)
                    pred.next=d_node.next
                    d_node.prev=pred
                    break

                i=i+1  
                n=n.next
    def removeKey(self,d_k):
        n=self.head.next
        while n is not self.head:
            if d_k==n.element:
                dkey=n.element
                n.element=None
                return dkey
          

            n=n.next            

           
                  
   
#Testing
print("\n//=======Testing=======//")
a = [10,20,30]
l1 = DoublyList(a)
print('===============================')
print('showlist')
l1.showList()
print('===============================')
print('insert_tail')
l1.insert_tail(30)         
l1.showList()
print('===============================')
print('insert')
l1.insert(60,2)
l1.showList()
print('===============================')
print('remove')
l1.remove(1)
l1.showList()
print('===============================')
print('removeKey')
print(l1.removeKey(10))



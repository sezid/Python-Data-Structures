class Node:
    def __init__(self,e,r):
        self.value=e
        self.next=r

class MyList:
    def __init__(self,a):
        if len(a)==0:
            self.head=None
            return None
        self.head=Node(a[0],None)
        tail=self.head
        i=1
        while i<len(a):
            n=Node(a[i],None)
            tail.next=n
            tail=n
            i=i+1
        return None
    def showList(self):
        n=self.head
        while (n is not None):
            print(n.value)
            n=n.next
    
    def isEmpty(self):
        if self.head is not None:
            return False
        else:
            return True     

    def clear(self):
        self.head=None
        return self.head

    def NodeAt(self,idx):
        if idx<0 and idx>=len(self.head):
            return None
        
        i=0
        n=self.head
        while n is not None:
            if idx==i:
                return n
            n=n.next
            i=i+1        
             
    def inserttail(self,newElement):#inserts in tail
        g=''
        n=self.head
        x=Node(newElement,None)
        j=self.head #counter
        while j is not None:
            if j.value==newElement:
                g='True'
                return g
                break
            j=j.next  
        if g!='True':
            while n.next is not None:
                n=n.next
            n.next=x  

    def insert(self,newElement,idx):
        n=self.head
        i=0
        if idx==0:
            x=Node(newElement,n)
            self.head=x
            return self.head
        while n is not None:
            if i==idx:
                pred=self.NodeAt(idx-1)
                suc=pred.next
                x=Node(newElement,suc)
                pred.next=x
            i=i+1
            n=n.next   

    def remove(self,dkey):
        i=0
        n=self.head
        if n is not None:
            if n.value==dkey:
                self.head=n.next
                return self.head
        
        while n is not None:
            if n.value==dkey:
                pred=self.NodeAt(i-1)
                r=self.NodeAt(i)
                suc=r.next
                pred.next=suc
                
                break
            
            i=i+1
            n=n.next
          
    def evenList(self):
        f=[]
        n=self.head
        while n is not None:
            if n.value%2==0:
                f.append(n.value)
            
            n=n.next
        return MyList(f)    

    def find(self,num):
        n=self.head
        while n is not None:
            if n.value==num:
                return True
            else:
                n=n.next        
        return False 

    def reverseList(self):
        newHead=None
        n=self.head
        
        while n is not None:
            nextNode=n.next
            n.next=newHead
            newHead=n
            n=nextNode
        self.head=newHead    
        return self.head

    #def sort(self):
        #max=0
        #n=self.head
        #while n is not None:
            #max=n.value
            #while

             
        
    def sum(self):
        x=0
        n=self.head
        while n is not None:
           x=x+n.value
           n=n.next
        return x    

    #def rotatektimes(self,num,d):#(incomplete)
        #n=self.head
        #if d=='left':
            
                   

#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = MyList(a)
l1.showList() #Should print: 10->20->30->40->50->60


#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) #Should print: false
b = []
l2 = MyList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) #Should print: true

#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() #Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList() #Should print: Empty List

#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = MyList(c)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90
l3.inserttail(100)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.insert(0, 0)
l3.showList() #Should print: 0->10->20->30->40->50->60->70->80->90->100
l3.insert(110, 5)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100
l3.insert(120, 12)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.inserttail(50) #Should print: Key 50 already exists

#Task-2.7 -- Remove
print("\n//=======Task 2.7 -- Remove=======//")
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(0)
l3.showList() #Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(110) 
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100->120
l3.remove(120)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.remove(120) #Should print: Key 120 does not exist

#Task-2.8 -- EvenList
print("\n//=======Task 2.8 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
l4 = MyList(d)
l5 = l4.evenList()
l5.showList() #Should print: 2->8​
#Task-2.9 -- Find
print("\n//=======Task 2.9 -- Find =======//")
found = l4.find(5)
print(found) #Should print: true
found = l4.find(4)
print(found) #Should print: false

#Task-2.10 -- Reverse List
print("\n//=======Task 2.10 -- Reverse =======//")
print("Before Reverse: ", end='')
l4.showList() #Should print: 1->2->5->3->8
l4.reverseList()
print("After Reverse: ", end='')
l4.showList() #Should print: 8->3->5->2->1


#Task-2.12 -- Sum of Elements
print("\n//=======Task 2.12 -- Sum of Elements =======//")
l4.showList() #Should print: 1->2->3->5->8
total = l4.sum()
print("Sum of Elements:", total)




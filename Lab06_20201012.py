print('----------Selection sort(Recursive)----------')
def selection_sort(a,i,j):
  l=len(a)
  if i==l and j==l:
    return a
  elif i<l-1:
    min=i
    while j<l:
      if a[j]<a[min]:
        min=j
      j=j+1

    if min!=i:
      temp=a[i]
      a[i]=a[min]
      a[min]=temp
    
    selection_sort(a,i+1,i+2)

a=[30,4,70,8,20,99]

selection_sort(a,0,1)
print(a)
print('----------Insertion sort(Recursive)----------')
def insertion_sort(a,i):
  l=len(a)
  if i==l:
    return a
  elif i<l:
    j=i-1
    x=a[i]
    while j>=0 and x<a[j]:
      a[j+1]=a[j]
      j=j-1
    a[j+1]=x
    insertion_sort(a,i+1)

#Tester
a=[60,50,44,2,7,10]
insertion_sort(a,1)
print(a)
print('----------Bubble sort and selection sort of singly linked list----------')
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
    def len_list(self):
        x=0
        n=self.head
        if n is None:
            return 0
        
        else:
            while n is not None:
                x=x+1
                n=n.next
            return x

    def bubble_sort(self,l):
        for i in range(l-1):
            curr=self.head
            nxt=curr.next
            prev=None
            while nxt is not None:
                if curr.value>nxt.value:
                    if prev==None:
                       prev=curr.next
                       nxt=nxt.next
                       prev.next=curr
                       curr.next=nxt
                       self.head=prev
                    else:   
                        temp=nxt
                        nxt=nxt.next
                        prev.next=curr.next
                        prev=temp
                        temp.next=curr
                        curr.next=nxt
                else:           
                    prev=curr
                    curr=nxt
                    nxt=nxt.next


                        
    def selection_sort(self):
     
      n=self.head
     
      while n is not None:
         
        min=n
        g=n.next
        
        while g is not None:
            if min.value>g.value:
                min=g
            
            g=g.next
        z=min.next    

        x=n
        min.next=n
        x.next=z
        n=n.next


a = [10,3,2,6,7]
l1 = MyList(a)
h=l1.head
l=l1.len_list()
print('Bubble sort')
l1.bubble_sort(l)
l1.showList()
print('Selection sort')
l1.selection_sort()
l1.showList()

#doubly linked list
print('-----------Doubly Linked List insertion sort---------')
class Node:  
    def __init__(self,value):  
        self.value=value;  
        self.prev=None;  
        self.next=None;  


class DoublyList:  
    
    def __init__(self):  
        self.head=None;  
        self.tail=None;  

    def add_node(self,data):  
      
        newNode = Node(data);  
        if(self.head==None):  
            self.head=self.tail=newNode;  
            self.head.prev=None;              
            self.tail.next=None;  
        else:              
            self.tail.next=newNode;              
            newNode.prev=self.tail;              
            self.tail=newNode;               
            self.tail.next=None;  

    def print_list(self):      
      n=self.head
      while n is not None:
        print(n.value)
        n=n.next

    def getNode(self,i):
      n=self.head
      if n==None:
        return None
      elif n.next is None:
        return n
      else:
        c=0
        while n is not None:
          if c==i:
            return n
          c=c+1
          n=n.next  


    def length(self):
      n=self.head
      c=0
      while n is not None:
        c=c+1
        n=n.next
      return c 

    def insert_sort(self,i=1):
      l=self.length()
      while i<l:
        c=i-1
        x1=self.getNode(i)
        while c>=0 and self.getNode(i).value<self.getNode(c):
            x2=self.getNode(c)
            temp=x1.value
            x1.value=x2.value
            x2.value=temp
            c=c-1
            




            
                 

#Incomplete

l2= DoublyList()    
l2.add_node(63)  
l2.add_node(23)  
l2.add_node(10)  
l2.add_node(4)  
l2.add_node(5)  
print(l2.getNode(0).value)
#l2.print_list()   



print('-----------Binary Search-----------------')
def binarySearch(a,l,r,val):

  mid=(l + r)// 2
  if a[mid]==val:
    return mid
  elif a[mid]>val:
    return binarySearch(a,l,mid-1,val)
  else:
    return binarySearch(a,mid+1,r,val)
 
a = [2, 3, 8, 10, 40]
print('The index is:',binarySearch(a,0,len(a)-1,10))

print('----------- Memoization of fibonacci-----------------')

b=[]
def n_fib(n):
  if b[n]>0:
    return b[n]
  elif n==0 or n==1:
    return 1
  else:
    return b[n].append(n_fib(n-1)+n_fib(n-2))

def calcfib():
  b.insert(0,1)
  b.insert(1,1)
  for i in range(2,11):
    b.insert(i,b[i-1]+b[i-2])

n=10
calcfib()
print('n='+str(n)+' Fibonacci',n_fib(n))


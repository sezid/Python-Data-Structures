#Programming Language: Pyhton 3.9

#Very Easy
print('______VERY EASY_____')
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
#TEST                
print('_______FACTORIAL______')
print('n=3 --->',factorial(3))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#TEST        
print('_______FIBONACCI______')
print('n=2 ----->',fibonacci(4))

def print_array(a,s=0):
    if s==len(a):
        return 
    else:
        print(a[s])
        return print_array(a,s=s+1)
#TEST        
print('_______PRINT AN ARRAY______')
b=[1,2,4,5]
print_array(b)


def powerN(a,n):
    if n==0:
        return 1
    else:
        return a*powerN(a,n-1)
#TEST
print('_______Power to N______')
print('3**1 =>',powerN(3,1))
print('3**2 =>',powerN(3,2))
print('3**3 =>',powerN(3,3))

#Easy
print('______EASY_____')
def dec_to_bin(n):
    if n>1:
        return dec_to_bin(n//2)+str(n%2)
    else:
        return str(n)
#TEST                
print('_______Decimal to Binary______')
print('20 --->',dec_to_bin(20))

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

    def sum_linked_list(self,h,s=0):
        if h is not None:
            s=s+h.value
            return self.sum_linked_list(h.next,s)
        else:
            return s
        

    def reverse_list(self,h):
        if h is None:
            return None
        elif h.next==None:
            self.head=h
            return
        else:
            self.reverse_list(h.next)  
            temp=h.next
            temp.next=h
            h.next=None
            
#TEST            
l=[1,2,3,4,5]
f=MyList(l)
h=f.head
print('_______Sum of linked list values______')
print(f.sum_linked_list(h))
print('_______Reverse a linked list______')
f.reverse_list(h)
f.showList()


#Medium
print('______MEDIUM_____')
def hocBuilder(height):
    if height==0:
        return 0
    elif height==1:
        return 8+hocBuilder(height-1)
    else:
        return 5+hocBuilder(height-1)
#TEST        
print('_______HOC BUILDER______')
print('height=1  ---->',hocBuilder(1))
print('height=2  ---->',hocBuilder(2))
print('height=3  ---->',hocBuilder(3))

                
#Hard
print('______HARD_____')
def triangle_forward(n,x=1,y=''):
    if x<=n:
        print(y+str(x))
        return triangle_forward(n,x=x+1,y=y+str(x))
    else:
        return

def triangle_backward(n,x=1,y=''):
    s=n-x
    if x<=n:
        print(s*' '+y+str(x))
        return triangle_backward(n,x=x+1,y=y+str(x))
    else:
        return
#TEST
print('_______PRINT TRIANGLE FORWARD______')
triangle_forward(5)
print('_______PRINT TRIANGLE BACKWARD______')
triangle_backward(5)


#Very Hard

print('______VERY HARD_____')
class FinalQ: 
    def print(self,array,idx): 
        if(idx<len(array)): 
            profit = self.calcProfit(array[idx])
            print('Investment:'+str(array[idx])+';','Profit: '+str(profit))
            return self.print(array,idx+1)
        else:
            return


  
    def calcProfit(self,investment):
        if investment==25000:
            return 0
        elif investment<=100000:
            return 4.5+self.calcProfit(investment-100)    
        elif investment>100000:
            return 8+self.calcProfit(investment-100)


#Tester 
array=[25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,0)





     




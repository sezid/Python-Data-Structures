#Task_1
class Stack_array:
    stack=[]
    pointer=-1

    def push(self,element):
        self.stack.append(element)
        self.pointer=self.pointer+1

    def peek(self):
        return (self.stack[self.pointer])

    def pop(self):
        value=self.stack[self.pointer]
        self.stack=self.stack[:-1]
        self.pointer=self.pointer-1
        return value        

    def call_stack(self):
      return self.stack

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False    
    def call_stack(self):
        return self.stack
#Task_2        
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack_linked_list:
    head=None
    
    def push(self,element):
        if self.head==None:
            self.head=Node(element)
        else:
            n=Node(element)
            n.next=self.head
            self.head=n    
        
    def peek(self):
        if self.head==None:
            return None
        else:    
            return self.head.value

    def pop(self):
        p_value=self.head
        self.head=self.head.next
        p_value.value=None
        p_value.next=None
        

    

    def isEmpty(self):
        if self.head is not None:
            return False
        else:
            return True   
    






print('Test_Array') 
print('========== Equation 1 ==============') 
st='1+2*[3/4)'
x=Stack_array()
dict1={']':'[','}':'{',')':'('}
for s in st:
    if s in dict1.values():
        x.push(s)
    elif s in dict1.keys():
        j=x.peek()
        if x.isEmpty()==False and dict1[s]==j:
            x.pop() 
if x.isEmpty()==True:
    print('The expression is correct')        
else:
    print('The expression is NOT correct')

print(x.call_stack())

print('========== Equation 2 ==============')
st='1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14'
x=Stack_array()
dict1={']':'[','}':'{',')':'('}
for s in st:
    if s in dict1.values():
        x.push(s)
    elif s in dict1.keys():
        j=x.peek()
        if x.isEmpty()==False and dict1[s]==j:
            x.pop() 
if x.isEmpty()==True:
    print('The expression is correct')        
else:
    print('The expression is NOT correct')
print('========== Equation 3 ==============')
st='1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
x=Stack_array()
dict1={']':'[','}':'{',')':'('}
for s in st:
    if s in dict1.values():
        x.push(s)
    elif s in dict1.keys():
        j=x.peek()
        if x.isEmpty()==False and dict1[s]==j:
            x.pop() 
            
if x.isEmpty()==True:
    print('The expression is correct')        
else:
    print('The expression is NOT correct')



print('Test_Linked_list')
print('========== Equation 1 ==============') 
st='1+2*(3/4)'
y=Stack_linked_list()
dict2={']':'[','}':'{',')':'('}
for s in st:
    if s in dict2.values():
        y.push(s)
    elif s in dict2.keys():
        t=y.peek()
        if dict2[s]==t and y.isEmpty()==False:
            y.pop()

if y.isEmpty()==True:
    print('The expression is correct')        
else:
    print('The expression is NOT correct')

print('========== Equation 2 ==============')
st='1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
y=Stack_linked_list()
dict2={']':'[','}':'{',')':'('}
for s in st:
    if s in dict2.values():
        y.push(s)
    elif s in dict2.keys():
        t=y.peek()
        if dict2[s]==t and y.isEmpty()==False:
            y.pop()

if y.isEmpty()==True:
    print('The expression is correct')        
else:
    print('The expression is NOT correct')

print('========== Equation 3 ==============')
st='1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
y=Stack_linked_list()
dict2={']':'[','}':'{',')':'('}
for s in st:
    if s in dict2.values():
        y.push(s)
    elif s in dict2.keys():
        t=y.peek()
        if dict2[s]==t and y.isEmpty()==False:
            y.pop()

if y.isEmpty()==True:
    print('The expression is correct')        
else:
    print('The expression is NOT correct')

#Programming Language: Pyhton 3.8


#Number 1 (Linear Array)
#Shift Left k cells
source=[10,20,30,40,50,60]
def shiftLeft(s,k):
  i=0
  for c in range(len(s)):
    if i-k<0:
      s[i]=0
    else:
      temp=s[i]
      s[i-k]=temp
      s[i]=0

    i=i+1    
  
shiftLeft(source,3)
print(source)





#Number 2 (Linear Array)
#Rotate Left k cells
source=[10,20,30,40,50,60]

def rotateLeft(s,k):
  lost=[]
  i=0
  for c in range(len(s)):
    if i-k<0:
      lost.append(s[i])
      
    else:
      temp=s[i]
      s[i-k]=temp
      s[i]=lost[(i-k)] 
    i=i+1   

rotateLeft(source,3)
print(source)




#Number 3 (Linear Array)
#Removing an element from an array
source=[10,20,30,40,50,0,0]

def remove(s,size,idx):
  i=0
  i2=0
  for c in range(size):
    if i==idx:
      s[i]=0
  
    i=i+1
  for c in range(size):
    if s[i2]==0:
      temp=s[i2]
      s[i2]=s[i2+1]
      s[i2+1]=temp
    i2=i2+1  

remove(source,5,2)
print(source)





#Number 4 (Linear Array)
#Remove all occurences of a particular element from an array
source=[10,2,30,2,50,2,2,0,0]

def removeAll(s,size,element):
  lst=[]
  i=0
  
  for c in range(size):
    if s[i]==element:
      s[i]=0
    i=i+1
   
    
  for n in range(len(s)):
    if s[n]!=0:
      lst.append(s[n])
      s[n]=0
    else:
      continue   
  for x in range(len(lst)):
    s[x]=lst[x]

removeAll(source,7,2)
print(source)





#Number 5 (Linear Array)
#Splitting an Array
leftsum=0
rightsum=0
s=input('Enter with space in between:')
x=s.split()

if len(x)%2!=0: #for odd length list
#midindex_no
  m=int(len(x)/2)

  for c in range(len(x)):
    leftsum=leftsum+int(x[c])
    rightsum=rightsum+int(x[(len(x)-1)-c])
    if c==m:
      if leftsum+int(x[2])==rightsum:
        print('True')
        break
      elif rightsum+int(x[2])==leftsum:
        print('True')
        break
      else:
        print('False')
        break

else: #for even length list
  v=int(len(x)/2)

  for c in range(v):
    leftsum=leftsum+int(x[c])
    rightsum=rightsum+int(x[(len(x)-1)-c])
    
  if leftsum==rightsum:
    print('True')
    
  else:
    print('False')





#Number 7 (Linear Array)
#Max Bunch Count
s=input('Enter with space in between:')
x=s.split()

recur_val=''
recur_val_count=0
max_bunch=0


for c1 in x:
  if c1!=recur_val:
    recur_val=c1
    recur_val_count=0
    recur_val_count=recur_val_count+1
  else:
    recur_val_count=recur_val_count+1

  if recur_val_count>max_bunch:
    max_bunch=recur_val_count    
     

print(max_bunch)





#Number 8 (Linear Array)
#Repetition
s=input('Enter with space in between:')
x=s.split()
dict1={}
dict2={}
for c in x:
  if c not in dict1.keys():
    dict1[c]=1
  else:
    dict1[c]=dict1[c]+1

j=dict1.values()
for c in j:
  if c not in dict2.keys():
    dict2[c]=1
  else:
    dict2[c]=dict2[c]+1  

for c in dict2.values():
  if c>=2:
    print('True')
    break
  else:
    print('False')
    break     





#Number 9 (Circular Array)
#Palindrome 
s=[10,20,0,0,0,10,20,30]

def palindrome(c1,start,size):
  count_match=0
  l_index=(start+size-1)%len(c1)
  

  for c in range(int(size/2)):

    if c1[start]==c1[l_index]:
      l_index=l_index-1
      start=start+1
      count_match=count_match+1

    elif l_index<0 and start>=len(c1):
      start=0
      l_index=len(c1)-1
    
  

  if count_match==int(size/2):
    return True
  else:
    return False  

palindrome(s,5,5)





#Number 10 (Circular Array)
#Intersection
def intersection(c1,s_1,size_1,c2,s_2,size_2):
  match_lst=[]
  l1=[]
  l2=[]

  for c in range(size_1):
    if s_1>=len(c1):
      s_1=0
    else:
      l1.append(c1[s_1])
      s_1=s_1+1
  for c in range(size_2):
    if s_2>=len(c2):
      s_2=0
    else:
      l2.append(c2[s_2])
      s_2=s_2+1  

  for c in l1:
    if c in l2:
      match_lst.append(c)


  return match_lst

c1=[40,50,0,0,0,10,20,30]
c2=[10,20,5,0,0,0,0,0,5,40,15,25]

intersection(c1,5,5,c2,8,7)





#Number 11 (Circular Array)
#Musical chair game
import random
source=['a','b','c','d','e','f','g']
import random
def remove_player(s,index):
  new=[]
  for c in range(len(s)):
    if c!=index:
      new.append(s[c])
  return new 


while True:

  x=random.randint(0,3) #gives random number
  if len(source)==1:
    print(source[0])
    break
  else:  
    if x==1:
  #remove player
      index_remove=int(len(source)/2)
      source=remove_player(source,index_remove)
    else:
  #rotate_right
      l_index=len(source)-1
      temp=source[l_index]  
  
      while l_index>0:
        source[l_index]=source[l_index-1]

        l_index=l_index-1
      source[0]=temp  
   
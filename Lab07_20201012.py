class KeyIndex:
    def __init__(self,a):
        self.k=[]
        sign='+ve'
        self.b=0
#to find if negative in given array
        for c in x:
            if c<0:
                sign='-ve'
                break
        if sign=='-ve':
            self.b=min(x)*-1    
            for c in range(len(x)):
                x[c]=x[c]+self.b    
        
        maximum=max(a)
            
        for d in range(maximum+1):
            self.k.append(0)
        for c in a:
            if self.k[c]!=0:
                self.k[c]=self.k[c]+1
            else:
                self.k[c]=1    
    

    def sort(self):
        sorted=[]
        
        for c in range(len(self.k)):
            if self.k[c]!=0:
                if self.k[c]>1:
                    for f in range(self.k[c]):
                        sorted.append(c-self.b)
                else:
                    sorted.append(c-self.b)
        return sorted                 
    
    def search(self,val):
        sorted=self.sort()
        if val in sorted:
            return 'True'
        else:
            return 'False'    

class hastable:
    def __init__(self,a):
        self.k=[]
        vowel=['a','e','i','o','u','E','A','I','O','U']
        digit=['1','2','3','4','5','6','7','8','9','0']
        consonant=0
        no_digit=0
        self.hash_val=[]
        for c in a:
            for i in c:
                if i in vowel:
                    continue
                elif i in digit:
                    no_digit=no_digit+1
                else:
                    consonant=consonant+1    
            hash_no=(consonant*24+no_digit)%9
            self.hash_val.append(hash_no)
            consonant=0
            no_digit=0            

        #constructing hash array
        start=min(self.hash_val)
        size_of_array=max(self.hash_val)
        for c in range(size_of_array+1):
            self.k.append(0)
        
        for c in range(len(a)):
            i=self.hash_val[c]
            while True:
                if self.k[i]==0:
                    self.k[i]=a[c]
                    break
                elif i>=len(self.k):
                    i=0
                else:
                    i=i+1    


    def show(self):
        return self.k







####Test######
print('-------------Key Index Search and Sort---------------')        
x=[-10,0,0,-6,4,5,4]                           
l1=KeyIndex(x)
print('-----Sort-----')
print(l1.sort())
print('-----Search-----')
print(l1.search(-5))    

print('-------------Hashtable---------------')
w=['ABYL37','ABJL37','KLERR43']
l2=hastable(w)
print(l2.show())      
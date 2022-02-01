#Programming Language: Python
class Node:
    def __init__(self,e,left,right,p):
        self.e=e
        self.left=left
        self.right=right
        self.p=p

#TREE_1
root1=Node(10,None,None,None)
n2=Node(5,None,None,None)
n3=Node(7,None,None,None)
n4=Node(17,None,None,None)
n5=Node(9,None,None,None)
n6=Node(28,None,None,None)
root1.left=n2
n2.p=root1
root1.right=n3
n3.p=root1
n2.left=n4
n4.p=n2
n2.right=n5
n5.p=n2
n3.right=n6
n6.p=n3
#TREE_2
root2=Node(103,None,None,None)
l2=Node(53,None,None,None)
l3=Node(72,None,None,None)
l4=Node(172,None,None,None)
l5=Node(93,None,None,None)
l6=Node(283,None,None,None)
root2.left=l2
l2.p=root2
root2.right=l3
l3.p=root2
l2.left=l4
l4.p=l2
l2.right=l5
l5.p=l2
l3.right=l6
l6.p=l3


class Tree:
    def height(self,r):
        if r==None:
            return 0

        else:
            return 1+max(self.height(r.left),self.height(r.right))

    def max(self,l,r):
        if l>r:
            return l
        else:
            return r    
    def level(self,n):
        if n.p==None:
            return 0
        else:
            return 1+self.level(n.p)    
    def print_preorder(self,r):
        if r!=None:
            print(r.e)
            self.print_preorder(r.left)
            self.print_preorder(r.right)

    def print_in_order(self,r):
        if r!=None:
            self.print_in_order(r.left)
            print(r.e)
            self.print_in_order(r.right)

    def print_post_order(self,r):
        if r!=None:
            self.print_in_order(r.left)
            self.print_in_order(r.right)
            print(r.e)

    def compare_tree(self,r1,r2):
        if r1==None and r2==None:
            return True
        elif (r1==None and r2!=None) or (r1!=None and r2==None):
            return False
        elif r1.e!=r2.e:
            return False
        else:
            return self.compare_tree(r1.left,r2.left) and self.compare_tree(r1.right,r2.right)             
    def copy_tree(self,r):
        if r==None:
            return None
        else:
            new_root=r
            new_root.left=self.copy_tree(r.left)
            new_root.right=self.copy_tree(r.right) 
        return new_root       

#GRAPH
class Node2:
    def __init__(self,e,l,r,m):
        self.e=e
        self.left=l
        self.right=r
        self.middle=m
    

#Tree for the Graph of given matrix
a=Node2('A',None,None,None)
b=Node2('B',None,None,None)
c=Node2('C',None,None,None)
d=Node2('D',None,None,None)
e=Node2('E',None,None,None)
f=Node2('F',None,None,None)
g=Node2('G',None,None,None)
a.left=d
a.middle=e
a.right=b
d.left=g
d.middle=f
d.right=c
f.middle=d
b.middle=g
g.middle=e
g.left=f



#TEST CLASS for tree                      
tree=Tree()
print('-----TREE-----')
print('------Height--------')
print('The Height is: '+str(tree.height(root1)))
print('------LEVEL--------')
print('The level is: '+str(tree.level(n4)))
print('-----pre_order-----')
tree.print_preorder(root1)
print('-----in_order-----')
tree.print_in_order(root1)
print('-----post_order-----')
tree.print_post_order(root1) 
print('----Compare----')
print(tree.compare_tree(root1,root2))
print('-----Copy tree and print-----')
new_root1=tree.copy_tree(root1)
tree.print_preorder(new_root1)
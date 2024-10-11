# assignment: programming assignment 3
# author: Nathan Tran
# date: 05/15/23
# file: tree.py consists of BinaryTree and ExpTree with methods
# input: parameters
# output: returns number

from stack import Stack
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        try:
            return self.rightChild
        except:
            return None
    
    def getLeftChild(self):
        try:
            return self.leftChild
        except:
            return None
    
    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

    def __str__(self):
        left = ''
        right = ''
        if self.leftChild != None:
            left = str(self.leftChild)
        if self.rightChild != None:
            right = str(self.rightChild)

        return f'{str(self.key)}({left})({right})'


class ExpTree(BinaryTree): 
    def make_tree(postfix):
        s = Stack()
        operator = ['^', '*', '/', '+', '-', '(', ')']
        for i in postfix:
            if i.isdigit() or '.' in i:
                s.push(ExpTree(i))
            if i in operator:
                temp = ExpTree(i)
                temp.rightChild = s.pop()
                temp.leftChild = s.pop()
                s.push(temp)
        return s.pop()

    def preorder(tree):
        s = ''
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def postorder(tree):
        s = ''
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s

    def inorder(tree):
        operator = ['^', '*', '/', '+', '-']
        s =''
        if tree != None:
            if tree.getRootVal() in operator:
                s += '(' + ExpTree.inorder(tree.getLeftChild())
                s += tree.getRootVal()
                s += ExpTree.inorder(tree.getRightChild()) + ')'
            else:
                s += ExpTree.inorder(tree.getLeftChild())
                s += tree.getRootVal()
                s += ExpTree.inorder(tree.getRightChild())
        return s
    
    def evaluate(tree):
        operator = ['^', '*', '/', '+', '-',]
        if tree != None:
            if tree.key not in operator:
                return tree.key
            else:
                left = float(ExpTree.evaluate(ExpTree.getLeftChild(tree))) 
                right = float(ExpTree.evaluate(ExpTree.getRightChild(tree)))
                if left != None and right != None:
                    if tree.key == '+':
                        return left + right
                    elif tree.key == '-':
                        return left - right
                    elif tree.key == '*':
                        return left * right
                    elif tree.key == '/':
                        return left / right
                    elif tree.key == '^':
                        return left**right
                else:
                    return None

    def __str__(self):
        return ExpTree.inorder(self)

# if __name__ == '__main__':
#     # test a BinaryTree
#     r = BinaryTree('a')
#     assert r.getRootVal() == 'a'
#     assert r.getLeftChild()== None
#     assert r.getRightChild()== None
#     assert str(r) == 'a()()'
#     r.insertLeft('b')
#     assert r.getLeftChild().getRootVal() == 'b'
#     assert str(r) == 'a(b()())()'
#     r.insertRight('c')
#     assert r.getRightChild().getRootVal() == 'c'
#     assert str(r) == 'a(b()())(c()())'
#     r.getLeftChild().insertLeft('d')
#     r.getLeftChild().insertRight('e')
#     r.getRightChild().insertLeft('f')
#     assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
#     assert str(r.getRightChild()) == 'c(f()())()'
#     assert r.getRightChild().getLeftChild().getRootVal() == 'f'
#     # test an ExpTree
#     postfix = '5 2 3 * +'.split()
#     tree = ExpTree.make_tree(postfix)
#     assert str(tree) == '(5+(2*3))'
#     assert ExpTree.inorder(tree) == '(5+(2*3))'
#     assert ExpTree.postorder(tree) == '523*+'
#     assert ExpTree.preorder(tree) == '+5*23'
#     assert ExpTree.evaluate(tree) == 11.0
#     postfix = '5 2 + 3 *'.split()
#     tree = ExpTree.make_tree(postfix)
#     assert str(tree) == '((5+2)*3)'
#     assert ExpTree.inorder(tree) == '((5+2)*3)'
#     assert ExpTree.postorder(tree) == '52+3*'
#     assert ExpTree.preorder(tree) == '*+523'
#     assert ExpTree.evaluate(tree) == 21.0
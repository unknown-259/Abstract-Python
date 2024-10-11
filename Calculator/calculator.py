# assignment: programming assignment 3
# author: Nathan Tran
# date: 05/15/23
# file: calculator.py is a program that allows the user to enter an expression and recieve an answer.
# input: user input from the keyboard
# output: prompts in the terminal telling the user information based on their input and/or a number

from stack import Stack
from tree import ExpTree

def infix_to_postfix(infix):
    infix = infix.replace("+", " + ")
    infix = infix.replace("-", " - ")
    infix = infix.replace("*", " * ")
    infix = infix.replace("/", " / ")
    infix = infix.replace("^", " ^ ")
    infix = infix.replace("(", "( ")
    infix = infix.replace(")", " )")
    infix = infix.split()
    prec = {'(':1, '+':2, '-':2, '*':3, '/':3, '^':4}
    opstack = Stack()
    postfix = []
    num = ''

    for i in infix:
        if i.isdigit() or '.' in i:
            num += i
            if (i.isdigit() or '.' in i) and i == infix[-1]:
                postfix.append(i)
        else:  
            postfix.append(num)
            num = ''
            if i == '(':
                opstack.push(i)
            elif i == ')':
                top = opstack.pop()
                while top != '(':
                    postfix.append(top)
                    top = opstack.pop()
            else:
                while not opstack.isEmpty() and (prec[i] <= prec[opstack.peek()]):
                    postfix.append(opstack.pop())
                opstack.push(i)

    while not opstack.isEmpty():
        postfix.append(opstack.pop())
    
    draft = ' '.join(postfix)
    split = draft.split()
    return ' '.join(split)
   
def calculate(infix):
    postfix = infix_to_postfix(infix)
    tree = ExpTree.make_tree(postfix.split()) 
    return ExpTree.evaluate(tree)

if __name__ == "__main__":
    print('Welcome to Calculator Program!')
    expression = input("Please enter your expression here. To quit enter 'quit' or 'q':\n").lower()
    while True: 
        if calculate(expression):
            print(calculate(expression))
        expression = input("Please enter your expression here. To quit enter 'quit' or 'q':\n").lower()
        if expression == 'quit' or expression == 'q':
            break
    print('Goodbye!')


# a driver to test calculate module
# if __name__ == '__main__':
#     # test infix_to_postfix function
#     print(infix_to_postfix('(5+2)*3'))
#     assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
#     assert infix_to_postfix('5+2*3') == '5 2 3 * +'
#     # test calculate function
#     assert calculate('(5+2)*3') == 21.0
#     assert calculate('5+2*3') == 11.0

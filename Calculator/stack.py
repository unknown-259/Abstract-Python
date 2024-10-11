# assignment: programming assignment 3
# author: Nathan Tran
# date: 05/15/23
# file: stack.py is a program with stack methods
# input: item from parameter
# output: adjustments to list or returns number

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    

# if __name__ == '__main__':
#     data_in = ['hello', 'how', 'are', 'you']
#     s = Stack()
#     for i in data_in:
#         s.push(i)
#     assert s.size() == len(data_in)
#     assert s.peek() == data_in[-1]
#     data_out = []
#     while not s.isEmpty():
#         data_out.append(s.pop())
#     assert data_out == data_in[::-1]
#     assert s.size() == 0
#     assert s.peek() == None

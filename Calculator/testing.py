class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    data = 'Hello! How are you?'
    print(data)

    d = Deque()    
    for i in data:
        if i.isalpha():
            d.addRear(i)
        else:
            d.addFront(i)
    while not d.isEmpty():
        print(d.removeFront(), end=', ')
        
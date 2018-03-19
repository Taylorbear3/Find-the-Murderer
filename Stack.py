class Stack :
    items = []
    def push(self,thing):
        self.items.append(thing)
    def pop(self):
        del(self.items[-1])
    def top(self):
        return self.items[-1]

books = Stack()
books.push("LOTR")

print(books.top())
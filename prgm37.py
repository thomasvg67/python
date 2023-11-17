class Publisher:
    def __init__(self,n):
        self.name = n
    def show(self):
        pass
class Book(Publisher):
    def __init__(self,t,a,n):
        self.title = t
        self.author = a
        Publisher.__init__(self,n)
    def show(self):
        pass
class Python(Book):
    def __init__(self,p,nop,t,a,n):
        self.price = p
        self.noOfPages = nop
        Book.__init__(self,t,a,n)
    def show(self):
        print("Book title : ",self.title)
        print("Author : ",self.author)
        print("Publisher : ",self.name)
        print("Price : Rs.",self.price)
        print("No of pages : ",self.noOfPages)
P1=Python(700,300,"Programming with Python","GV Rossum","ABC Books")
P1.show()
class Book :
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def summary(self):
        return f"'{self.title}' by {self.author}, published in {self.year}."

b1= Book("1984", "George Orwell", 1949)    
b2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(b1.summary())
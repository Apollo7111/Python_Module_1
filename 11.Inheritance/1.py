class Publication:
    def __init__(self, name,):
        self.name = name

    def information(self):
        # print(self.name)
        pass

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)
    def information(self):
        super().information()
        print(f"{self.name} (chief editor {self.chief_editor})")

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(name)

    def information(self):
        super().information()
        print(f"{self.name} (author {self.author}, {self.pages} pages)")


m1 = Magazine('Donald Duck', 'Aki Hyyppä')
b1 = Book('Compartment No. 6', 'Rosa Liksom', 192)

m1.information()
b1.information()
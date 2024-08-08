"""
Clases para gestionar los Libros,Autores y Prestamos del sistema.
"""
from datetime import timedelta,date

class Author(object):
    class_counter = 1
    def __init__(self,name):
        self.id= Author.class_counter
        self.name=name
        Author.class_counter +=1
        self.books=[]

class Book(object):
    class_counter = 1
    def __init__(self,title):
        self.id= Book.class_counter
        self.title=title
        Book.class_counter +=1
        self.author=None
        self.borrowed=False

class Borrow(object):
    class_counter = 1
    def __init__(self,book_obj,reader_name):
        self.id= Borrow.class_counter
        self.book=book_obj
        self.reader_name=reader_name
        self.date_borrowed= date.today()
        self.date_return=date.today()+timedelta(days=3)
        Borrow.class_counter +=1
"""
Programa principal del sistema.
"""
import os
from models import Author,Book,Borrow
from tabulate import tabulate

#bases de datos en memoria
db_books=[]
db_authors=[]
db_borrows=[]

def searchAuthor_by_book(title):
    for b in db_books:
                if b.title.lower() == title.lower():
                    return b.author
    return None

def searchAuthor_by_name(name):
    for b in db_authors:
                if b.name.lower() == name.lower():
                    return b
    return None

def bookIsBorrowed(book_id):
    for b in db_borrows:
        if b.book.id == id:
            return True
    return False

def searchBook_by_title(title):
    for b in db_books:
                if b.title.lower() == title.lower():
                    return b
    return None
def searchBook_by_id(id):
      for b in db_books:
            if b.id==id:
                  return b
      return None

def viewAuthors():
    if len(db_authors)>0:
        header= ['Id_Author','Nombre']
        rows=[]
        rows.append(header)
        for b in db_authors:
            rows.append([b.id,b.name])
        print(tabulate(rows, headers='firstrow', tablefmt='fancy_grid'))
    else:
         print("*** No hay Autores en la biblioteca ***")  

def viewBooks():
    if len(db_books)>0:
        header= ['Id_Libro','Titulo_del_libro','Id_Autor','Nombre_autor','Estatus']
        rows=[]
        rows.append(header)
        for b in db_books:
            rows.append([b.id,b.title,b.author.id,b.author.name, 'Prestado' if b.borrowed else 'disponible' ])
        print(tabulate(rows, headers='firstrow', tablefmt='fancy_grid'))
    else:
         print("*** No hay libros en la biblioteca ***") 
          
def addBook():
      book_title=input("Por favor proporciona un titulo para el libro: ")
      if searchBook_by_title(book_title) is not None:
          respuesta=input("Ese titulo ya existe en la libreria, deseas agregar otra copia? (Si/No): ") 
          if respuesta.lower()=="si":
            new_book=Book(book_title)
            author_record=searchAuthor_by_book(book_title)
            print(f"author_record={author_record}")
            if author_record is None:
               print("No se encontro al Autor")
                # print("No existe el Autor")
                # new_author=Author(author_name)
                # new_book.author=new_author
                # new_author.books.append(new_book)
                # db_books.append(new_book)
                # db_authors.append(new_author)
                # print("Libro agregado")
                # table = [['Id_libro','Titulo_Libro','Id_Autor','Nombre_Autor'], [new_book.id,new_book.title,new_book.author.id,new_book.author.name]]
                # print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            else:
                new_book.author=author_record
                #author_record.books.append(new_book)
                db_books.append(new_book)
                print("Libro agregado")
                table = [['Id_libro','Titulo_Libro','Id_Autor','Nombre_Autor'], [new_book.id,new_book.title,new_book.author.id,new_book.author.name]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
      else:
            new_book=Book(book_title)
            author_name=input("Por favor proporciona el nombre del autor: ")
            author_record=searchAuthor_by_name(author_name)
            print(f"author_record={author_record}")
            if author_record is None:
                print("No existe el Autor")
                new_author=Author(author_name)
                new_book.author=new_author
                new_author.books.append(new_book)
                db_books.append(new_book)
                db_authors.append(new_author)
                print("Libro agregado")
                table = [['Id_libro','Titulo_Libro','Id_Autor','Nombre_Autor'], [new_book.id,new_book.title,new_book.author.id,new_book.author.name]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            else:
                new_book.author=author_record
                author_record.books.append(new_book)
                db_books.append(new_book)
                print("Libro agregado")
                table = [['Id_libro','Titulo_Libro','Id_Autor','Nombre_Autor'], [new_book.id,new_book.title,new_book.author.id,new_book.author.name]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


def borrowBook():
    book_id=input("Proporciona el Id del libro que deseas prestar:")
    if book_id.isnumeric():
        book=searchBook_by_id(int(book_id))
        if book is None:
            print("No existe un libro con ese numero de id")
        else:
            #Generar el prestamo
            if not book.borrowed:
                reader_name = input("Proporcione su nombre: ")
                new_borrow=Borrow(book,reader_name)
                db_borrows.append(new_borrow)
                book.borrowed=True
                print("Se registro el prestamo")
                table = [['Id_libro','Titulo_Libro','Id_Autor','Nombre_Autor','Id_prestamo','Fecha_Prestamo','Fecha_devolucion'],[book.id,book.title,book.author.id,book.author.name,new_borrow.id,new_borrow.date_borrowed,new_borrow.date_return]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            else:
                print("Libro no disponible, ha sido prestado!")
    else:
         print("Id de libro invalido!!")

def viewBorrows():
    if len(db_borrows)>0:
        header= ['Id_Prestamo','Lector','Titulo_Libro','Nombre_Autor','Fecha_Prestamo','Fecha_Devolucion']
        rows=[]
        rows.append(header)
        for b in db_borrows:
            rows.append([b.id,b.reader_name,b.book.title,b.book.author.name,b.date_borrowed,b.date_return])
            #table = [['Book_Id','Book_Title','Author_id','Author_name'], [b.id,b.title,b.author.id,b.author.name]]
        print(tabulate(rows, headers='firstrow', tablefmt='fancy_grid'))
    else:
         print("*** No hay prestamos registrados ***")  

def main_menu():
    print("1.- Ver todos los Libros")
    print("2.- Ver todos los autores")
    print("3.- Agregar Libro")
    print("4.- Prestar Libro")
    print("5.- Consultar prestamos")
    print("6.- Salir")

def main():
    main_menu()
    option=0
    while option!="6":
        option=input("Por favor eliga una opcion:")
        match(option):
            case "1":
                    os.system('cls')
                    print("Elegiste ver los libros")
                    viewBooks()
                    main_menu()
            case "2":
                    os.system('cls')
                    print("Elegiste ver los autores")
                    viewAuthors()
                    main_menu()    

            case "3":
                    os.system('cls')
                    print("Elegiste Agregar libro")
                    addBook()
                    main_menu()
            case "4":
                    os.system('cls')
                    print("Elegiste Prestar libro")
                    borrowBook()
                    main_menu()
            case "5":
                    os.system('cls')
                    print("Elegiste consultar prestamos")
                    viewBorrows()
                    main_menu()
                    
            case "6":
                    print("Hasta Luego")
                    
            case _:
                    os.system('cls')
                    print("Opcion no valida")
                    main_menu()

if __name__== "__main__":
    print("Bienvenido al programa de prestamos de libros")
    main()
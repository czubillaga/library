from models.author import Author
from models.book import Book

from db.run_sql import run_sql
import repositories.author_repository as author_repository

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE * FROM books WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(author, row['title'], row['year'], row['genre'], row['id'])
        books.append(book)
    return books

def select(id):
    books = []
    sql = "SELECT * FROM books WHERE author_id=%s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(author, row['title'], row['year'], row['genre'], row['id'])
        books.append(book)
    return books

def update(book):
    sql = "UPDATE books SET (author, title, year, genre) = (%s,%s,%s,%s) WHERE id=%s"
    values = [book.author.name, book.title, book.year, book.genre, book.id]
    run_sql(sql, values)

def save(book):
    sql = "INSERT INTO books (author, title, year, genre, author_id) VAlUES (%s,%s,%s,%s,%s) RETURNING *"
    values = [book.author.name, book.title, book.year, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

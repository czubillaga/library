from models.author import Author
from models.book import Book

from db.run_sql import run_sql
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE * FROM authors WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors

def select(id):
    sql = "SELECT * FROM authors WHERE id=%s"
    values = [id]
    author = run_sql(sql, values)
    return author[0]

    

def update(author):
    sql = "UPDATE authors SET (name) = (%s) WHERE id=%s"
    values = [author.name, author.id]
    run_sql(sql, values)

def save(author):
    sql = "INSERT INTO authors (name) VAlUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author
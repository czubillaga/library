import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author('Michael Crichton')
author_repository.save(author1)

book1 = Book(author1, 'Jurassic Park', 1987, 'Science Fiction')

book_repository.save(book1)
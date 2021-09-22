from flask import Flask, render_template, redirect
from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from flask import Blueprint

library_blueprint = Blueprint('library', __name__)

@library_blueprint.route('/library')
def books():
    books = book_repository.select_all()
    return render_template('index.html', title = 'Books', books=books)


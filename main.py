from flask import Flask
from hello.hello_controller import hello_bp
from convert.convert_controller import convert_bp
from books.book_controller import books_bp
from form.form_controller import form_bp

app = Flask(__name__)

app.register_blueprint(hello_bp)
app.register_blueprint(convert_bp)
app.register_blueprint(books_bp)
app.register_blueprint(form_bp)


app.run(debug=True, port=5000)

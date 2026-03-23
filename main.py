from flask import Flask
from hello.hello_controller import hello_bp


app = Flask(__name__)

app.register_blueprint(hello_bp)

app.run(debug=True, port=5000)

# Imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# My App
app = Flask(__name__)



# Home Page
@app.route("/")
def index():
    return render_template("index.html")




if __name__ in "__main__":
    app.run(debug=True)


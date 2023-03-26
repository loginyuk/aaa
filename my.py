from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/my")
def my():
    return render_template('index.html', title='Trener')


if __name__ == '__main__':
    app.run(debug=True)


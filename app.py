from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for('index2.html'))

if __name__ == '__main__':
    app.run()

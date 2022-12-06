from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index2():  # put application's code here
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()

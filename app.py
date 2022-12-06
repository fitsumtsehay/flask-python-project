from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template("index2.html")

if __name__ == '__main__':
    app.run()

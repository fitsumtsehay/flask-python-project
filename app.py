from flask import Flask
app = Flask(__name__)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM propertylist")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', propertylist=data )

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1awondmu'
app.config['MYSQL_DB'] = 'crud'

# app.config['CLEARDB_DATABASE_URL']: mysql://b94702d367220f:7eb7542e@us-cdbr-east-06.cleardb.net/heroku_fac056f3b74a8df?reconnect=true
mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM propertylist")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', propertylist=data )

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        phone = request.form['phone']
        propertyaddress = request.form['propertyaddress']
        propertytype = request.form['propertytype']
        numberofbedrooms = request.form['numberofbedrooms']
        price = request.form['price']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO propertylist (name, phone, propertyaddress, propertytype, numberofbedrooms, price) VALUES (%s, %s, %s, %s, %s, %s)", (name, phone, propertyaddress, propertytype, numberofbedrooms, price))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM propertylist WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update',methods=['POST'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        propertyaddress = request.form['propertyaddress']
        propertytype = request.form['propertytype']
        numberofbedrooms = request.form['numberofbedrooms']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE propertylist
        SET name=%s, phone=%s, propertyaddress=%s, propertytype=%s, numberofbedrooms=%s, price=%s
        WHERE id=%s
        """, (name, phone, propertyaddress, propertytype, numberofbedrooms, price, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)

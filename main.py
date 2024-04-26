from flask import Flask, render_template, request, redirect, url_for
import db
import sqlite3
app = Flask(__name__)
DATABASE = 'database.db'
db.create_books_table()

@app.get('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close
    books = []
    for row in db_books:
        books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})
    return render_template(
        'index.html',
        books = books
        )
    
@app.get('/form')
def form():       
    return render_template(
        'form_html'
    )
@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?, ?, ?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))
    
    
@app.put('/test/<id>')
def put_test(id):
    print(id)
    return 'OK',200

@app.route('/test2', methods=['POST'])
def put_002():
    res = request.form.get("_method")
    if res == 'PUT':
        print('PUT TEST OK')

    return 'OK',200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5001' )
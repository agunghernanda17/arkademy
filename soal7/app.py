from flask import Flask, render_template
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "admin"
        db = "tes"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    def query(self):
        self.cur.execute("SELECT a.id as id,a.name as category_name,GROUP_CONCAT(CONCAT(b.name)SEPARATOR ',')AS products FROM categories a JOIN products b where b.category_id=a.id GROUP BY a.id,b.category_id ;")
        result = self.cur.fetchall()
        return result
    def tambah_category(self):
        self.cur.execute("INSERT INTO Categories(name)VALUES('Coba')")
        self.con.commit()
@app.route('/')

def query():
    def db_query():
        db = Database()
        emps = db.query()
        return emps
    res = db_query()
    return render_template('index.html', result=res, content_type='application/json')

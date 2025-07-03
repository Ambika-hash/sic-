import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(host='localhost', user="root", password="ambika", database='ambika', port=3306)
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('DB disconnection failed')

def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(30), phone_number	bigint unique, salary float, commission		float default(0), years_of_experience tinyint, technology		varchar(30)	not null)'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Table creation failed')

def read_all_employees():
    query = 'select * from employees'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrived')
        
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')
def add_to_table():
    query = "insert into table employees values("Rama") "
connection = connect_db()
create_table()
read_all_employees()
disconnect_db(connection)
# connection.close() # to disconnect the DB
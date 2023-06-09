"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

connect = psycopg2.connect(host='localhost', database='north', user='postgres', password='dem6600')

with connect.cursor() as cur:
    cur.execute('TABLE customers')
    customers = cur.fetchall()
    if len(customers) == 0:
        cur.execute('''COPY customers(customer_id, company_name, contact_name)
        FROM '/tmp/customers_data.csv'
        DELIMITER ','
    CSV HEADER;''')
with connect.cursor() as cur_:
    cur_.execute('TABLE employees')
    employees = cur_.fetchall()
    if len(employees) == 0:
        cur_.execute('''COPY employees(employee_id, first_name, last_name, title, birthdate, notes)
    FROM '/tmp/employees_data.csv'
    DELIMITER ','
    CSV HEADER;''')
with connect.cursor() as cur__:
    cur__.execute('TABLE orders')
    orders = cur__.fetchall()
    if len(orders) == 0:
        cur__.execute('''COPY orders(order_id, customer_id_, employee_id_, order_data, ship_city)
    FROM '/tmp/orders_data.csv'
    DELIMITER ','
    CSV HEADER;''')


connect.commit()
connect.close()

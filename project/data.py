import psycopg2
from psycopg2.extras import DictCursor
import sys

conn = psycopg2.connect("dbname=dbproject user=farbod password=123456")
cur = conn.cursor(cursor_factory = DictCursor)

kind_dict= {
    '00000000': "clothes",
    '00000100': "mobile/tablet"
}


def get_products():
    cur.execute('SELECT * FROM Product')
    for product in cur:
        product['kind']= kind_dict[product.get('kind')]
        yield product


def get_authors():
    cur.execute('SELECT * FROM bookauthor')
    for author in cur:
        yield author


def insert_customer(data):
    cur.execute('INSERT INTO Customer(FirstName,LastName,Username,\
    Password)VALUES(%s,%s,%s,%s);',\
     (data['first_name'], data['last_name'], data['username'],\
      data['password']))
    conn.commit()


def insert_product(data):
    cur.execute('INSERT INTO product(id, sellingprice, company,\
     discount, buyingprice, title, productiondate, kind)\
     VALUES(%s,%s,%s,%s,%s,%s,%s,%s);',(data['id'],\
      data['sellingprice'], data['company'], 0, data['buyingprice'],\
      data['title'],data['productiondate'],data['kind']))
    conn.commit()


def insert_order(data):
    cur.execute('INSERT INTO _order(customerid, id, cost, registerdate, \
    customeraddressid, deliverymanid ,  deliverydate)VALUES(%s,%s,%s,\
    %s,%s,%s,%s);',(data['customerid'],data['id'], data['cost'],\
     data['registerdate'],data['customeraddressid'],data.get('deliverymanid'),\
     data.get('deliverydate')))
    conn.commit()


def insert_order_product_relation(data):
    for item in data['selected_item']:
        print("---"+str(item), sys.stdout)
        cur.execute('INSERT INTO PO(customerid,orderid,productid,quantity)\
            VALUES(%s,%s,%s,%s);',(data['customerid'],data['id'], item, 1))
        conn.commit()

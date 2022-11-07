#Realizzare un sito web che permetta di visualizzare l'elenco dei primi 10 clienti che hanno speso di più. 
#Il maneger di BikeStore si collega alla rotta /bestCustomers e riceve l'elenco dei clienti.
#Cliccando poi sull'ID di uno dei clienti, si deve poter visualizzare l'elenco degli ordini effettuati. Utilizzare Bootstrap per l'interfaccia grafica.

from flask import Flask,render_template,request,send_file,make_response, url_for, Response,redirect
app = Flask(__name__)
import io
import geopandas
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import pymssql
import matplotlib.pyplot as plt
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='gallo.tristan', password='xxx123##', database='gallo.tristan')


@app.route("/bestCustomers", methods=["GET"])
def bestCustomers():
    query = 'SELECT TOP 10 customers.customer_id, customers.first_name, customers.last_name ,SUM(list_price) as spesa_totale FROM sales.customers INNER JOIN sales.orders ON sales.customers.customer_id = sales.orders.customer_id INNER JOIN sales.order_items ON sales.order_items.order_id = sales.orders.order_id GROUP BY customers.customer_id, customers.first_name, customers.last_name ORDER BY SUM(list_price) DESC '
    #INNER JOIN sales.oder_items ON sales.orders.order_id = sales.order_items.order_id
    tabella = pd.read_sql(query,conn)
    print(tabella.columns.values)
    return render_template("bestCustomers.html", nomiColonne = tabella.columns.values, dati = tabella.values)

@app.route("/totaleOrdini/<valore>")
def totaleOrdini(valore):
    query = f'SELECT * FROM sales.customers INNER JOIN sales.orders ON sales.customers.customer_id = sales.orders.customer_id WHERE customers.customer_id = {valore}'
    tabella = pd.read_sql(query,conn)
    return render_template("totaleOrdini.html", nomiColonne = tabella.columns.values, dati = tabella.values)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
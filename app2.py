#Realizzare un sito web ch epermetta di visualizzare le informazioni riguardanti i clienti.
#Un componente dello staff richiama la rotta /infoUser dove sono presenti due text per l'inserimento del nome e del cognome del cliente ed un bottone per inviare le informazioni,
#Una volta inviate, il sito risponde con tutte le informazioni relative a quel cliente, una sotto l'altra. 
#Se il cliente non esiste, deve essere visualizzato un opportuno messaggio di errore. Utilizzare Bootstrap per l'interfaccia grafica di tutte le pagine.

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


@app.route('/infoUser', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/risultato', methods=['GET'])
def risultato():
    Nome = request.args['Nome']
    Cognome = request.args['Cognome']
    query = f"select * from sales.customers where first_name = '{Nome}' and last_name = '{Cognome}' "
    df = pd.read_sql(query, conn)
    dati = list(df.values.tolist())
    if dati == []:
        return render_template('error.html')
    else:
        return render_template('result.html', nomiColonne = df.columns.values, dati = list(df.values.tolist()))
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
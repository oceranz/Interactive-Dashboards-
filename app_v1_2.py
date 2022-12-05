#Paso 1: Importar las librerias correspondientes
import dash #Importar la libreria dash
from dash import html
import dash_core_components as dcc

#Paso 2: Instanciar la aplicacion 
app=dash.Dash(__name__) 

#Paso 3: Agregar elementos de HTML 
app.layout=html.Div([
    html.H1('Poverty And Equity Database New',
            style={'color': 'blue',
                   'fontSize': '40px'})])

#Paso 4: Iniciar el servidor de la aplicacion 
if __name__ == '__main__':
    app.run_server(debug=True)
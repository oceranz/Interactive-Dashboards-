#Paso 1: Importar la libreria dash
import dash 
from dash import html #import dash_html_components as html forma obsoleta de importar la libreria de dash

#Paso 2: Instanciar la aplicacion
app=dash.Dash(__name__)

#Paso 3: Agregar elementos de HTML
app.layout = html.Div([
    html.H1('Mi primera aplicacion en Dash'),
    html.H2('Hola!!!......') 
])

#Iniciar el servidor de la aplicacion
if __name__ == '__main__':
    app.run_server(debug=True)
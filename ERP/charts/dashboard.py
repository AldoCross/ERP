import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

## Importar la data
df = pd.read_csv('data.csv', delimiter = ';')

#Crear una tabla dinámica
pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)

trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declinada')], name='Declinada')
trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pendiente')], name='Pendiente')
trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presentada')], name='Presentada')
trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'ganada')], name='Ganada')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Reporte de Funnel de Ventas'),
    html.Div(children='''Reporte Nacional de Ventas.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4],
            'layout':
            go.Layout(title='Estado de orden por cliente', barmode='stack')
        })
])


if __name__ == '__main__':
    app.run_server(debug=True)
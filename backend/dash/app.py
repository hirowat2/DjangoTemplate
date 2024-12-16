from django.apps import AppConfig
from dash import dcc, html
import plotly.express as px
from django_plotly_dash import DjangoDash

# Criar o app Dash
app = DjangoDash('SimpleDash')  # O nome do aplicativo

# Exemplo de gráfico: Gráfico de barras
df = px.data.gapminder()  # Dados de exemplo do Plotly
fig = px.bar(df, x="continent", y="pop", title="População por Continente")

app.layout = html.Div([
    html.H1("Dashboard Exemplo com Django e Plotly Dash"),
    dcc.Graph(id='bar-graph', figure=fig)
])

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dash'

    def ready(self):
        import dash.dash_app  # Garante que o app Dash seja carregado

from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from app import *
from dash_bootstrap_templates import ThemeSwitchAIO

#Styles =================================
url_theme1 = dbc.themes.VAPOR 
url_theme2 = dbc.themes.FLATLY
template_theme1 = 'vapor'
template_theme2 = 'flatly'

# Reading data ==========================
df = pd.read_csv('data_clean.csv')
state_options = [{'label': x, 'value': x} for x in df['ESTADO'].unique()]
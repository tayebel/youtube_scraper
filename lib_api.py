
api_key=input('Please enter your API key:')
from googleapiclient.discovery import build
import random as rd
import string
import numpy as np
import seaborn as sns
import pandas as pd
import dash
import matplotlib.pyplot as plt
from dash import Dash, html, dcc,dash_table,callback,Output,Input
import plotly.graph_objs as go
import plotly.express as px
import openpyxl
# Set up the API client
youtube = build('youtube', 'v3', developerKey=api_key)

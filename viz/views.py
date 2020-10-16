from django.shortcuts import render, redirect
import pandas as pd 
import numpy as np 
import plotly.graph_objs as go
import plotly.express as px
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output



# Create your views here.
def visual(request):
    if request.method == 'POST':
        plot_type = request.POST.get('plot-type')   
        x_axis = request.POST.get('x-axis') or None
        y_axis = request.POST.get('y-axis') or None
        color = request.POST.get('color') or None
        size = request.POST.get('size') or None
        names = request.POST.get('names') or None
        title = request.POST.get('title') or None

    # print(plot_type, x_axis, y_axis, color, size, names, title)
    
    fig = go.FigureWidget()

    context = {
        'fig':fig.to_html()
    }
    return render(request, 'viz/visual.html', context)





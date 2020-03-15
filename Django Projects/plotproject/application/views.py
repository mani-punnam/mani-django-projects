from django.shortcuts import render
import plotly.graph_objects as go
# Create your views here.
def view1(request):
    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.write_image('static/images/figure1.svg')
    return render(request,'application/sample.html')
def view3(request):
    fig=go.Figure(data=go.Bar(y=[2,3,1]))
    fig.write_html('templates/application/second_figure.html',config={'displayModeBar': False},auto_open=False)
    return render(request,'application/sample.html')
def view2(request):
    return render(request,'application/second_figure.html')

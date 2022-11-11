from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

df = px.data.tips()

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        if load_template in(['chart.html', 'plotly.html']):
            pie_fig = donut_chart()
            scatter_fig = scatter_chart()
            bar_fig = bar_chart()
            bubble_fig = bubble_chart()
            pie_plot_ = pie_fig.to_html(full_html=False, include_plotlyjs='cdn')
            scatter_plot_ = scatter_fig.to_html(full_html=False, include_plotlyjs='cdn')
            bar_plot_ = bar_fig.to_html(full_html=False, include_plotlyjs='cdn')
            bubble_plot_ = bubble_fig.to_html(full_html=False, include_plotlyjs='cdn')
            context['plot1'] = bar_plot_
            context['date'] = datetime.today().strftime('%Y-%m-%d')
            context['time'] = datetime.now().strftime("%H:%M:%S")
            context['plot2'] = pie_plot_
            context['plot3'] = scatter_plot_
            context['plot4'] = bubble_plot_
            context['segment'] = load_template
            html_template = loader.get_template('dashboards/' + load_template)
            return HttpResponse(html_template.render(context, request))

        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        pass
        #Insert 404 page if you have
    except:
        pass
    #insert 500 page if you have



# def get_pie_chart():
# # This dataframe has 244 lines, but 4 distinct values for `day`
#     fig = px.pie(df, values='tip', names='day',title="Plotly Pie chart example", color_discrete_sequence=px.colors.sequential.RdBu)
#     return fig

def donut_chart():
    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    return fig

def bar_chart():
    data = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             title="Plotly Bar chart example",
             labels={'pop':'population of Canada'}, height=400)
    return fig

def scatter_chart():
    fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="Plotly Scatter plot example")
    
    return fig


def bubble_chart():
    fig = px.scatter(px.data.gapminder().query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",title="Plotly bubble chart example",
                 hover_name="country", log_x=True, size_max=60)
    return fig
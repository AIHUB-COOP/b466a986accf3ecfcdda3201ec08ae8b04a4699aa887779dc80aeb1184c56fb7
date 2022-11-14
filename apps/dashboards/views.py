from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from .utils import get_geo, get_center_coordinates, get_zoom
import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

df = px.data.tips()

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

def render_charts(request):
    context = {}
    load_template = request.path.split('/')[-1]
    context['segment'] = load_template
    html_template = loader.get_template('dashboards/' + 'chart.html')
    return HttpResponse(html_template.render(context, request))


def render_plots(request):
    context = {}
    load_template = request.path.split('/')[-1]
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
    html_template = loader.get_template('dashboards/' + 'plotly.html')
    return HttpResponse(html_template.render(context, request))


# Create your views here.
def calculate_distance_view(request):
    # print('Im in here/////////////////')
    # initial values
    distance = None
    destination = None
    print('disthere', distance)
    obj = get_object_or_404(Measurement, id=1)
    # print('obj here', obj)
    form = MeasurementModelForm(request.POST or None)
    # print('form here', form)
    geolocator = Nominatim(user_agent='measurements')

    # ip = '72.14.207.99'
    ip = "173.242.180.236"
    # ip = get_ip_address(request)  # only works in production
    # print("ip------",ip)
    country, city, lat, lon = get_geo(ip)
    # print(ip)
    # print( 'oopsssssssssssss',country, city, lat, lon)
    location = geolocator.geocode(city)

    # location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # initial folium map
    m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)
    # location marker
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        # print(destination, "destttttttttttttt")

        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        # folium map modification
        m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))
        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)
        # destination marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
                    icon=folium.Icon(color='red', icon='cloud')).add_to(m)


        # draw the line between location and destination
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
        m.add_child(line)
        
        instance.location = location
        instance.distance = distance
        instance.save()
    
    m = m._repr_html_()

    context = {
        'distance' : distance,
        "current_location": f"{city.get('city')} ,{city.get('country_name')}",
        'destination': destination,
        'form': form,
        'map': m,
    }
    html_template = loader.get_template('dashboards/' + 'maps.html')
    return HttpResponse(html_template.render(context, request))

    # return render(request, 'measurements/main.html', context)
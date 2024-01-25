from django.shortcuts import render
import urllib.request
import json
from math import ceil
from datetime import datetime

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5c12c76377d5dccbf118e5359a569888').read()
        list_of_data = json.loads(source)

        data = {
            'city': str(city),
            'country_code': 'Uzbekistan',
            'temp': ceil(float(list_of_data['main']['temp']) - float(273.15)),
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': str(list_of_data['weather'][0]['icon'])
        }
        print(data)
    else:
        data = {}

    doy = datetime.today().timetuple().tm_yday

    # "day of year" ranges for the northern hemisphere
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    # winter = everything else

    if doy in spring:
        season = 'spring'
    elif doy in summer:
        season = 'summer'
    elif doy in fall:
        season = 'fall'
    else:
        season = 'winter'

    selected = "selected"

    return render(request, 'main.html', {"data": data, "season": season, "selected": selected})

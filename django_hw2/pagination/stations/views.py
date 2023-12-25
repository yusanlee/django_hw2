from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        read = csv.DictReader(file)
        for name in read:
            data.append(name)
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

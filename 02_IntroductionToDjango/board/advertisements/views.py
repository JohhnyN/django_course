from django.shortcuts import render


# Create your views here.


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def web_design_3(request, *args, **kwargs):
    return render(request, 'advertisement/web-design-3.html', {})


def devops(request, *args, **kwargs):
    return render(request, 'advertisement/devops.html', {})


def restaurant_manager(request, *args, **kwargs):
    return render(request, 'advertisement/restaurant-manager.html', {})


def excel_gsheets(request, *args, **kwargs):
    return render(request, 'advertisement/excel-gsheets.html', {})

def music_manager(request, *args, **kwargs):
    return render(request, 'advertisement/music-manager.html', {})
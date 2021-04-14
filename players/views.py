from django.shortcuts import render, redirect
from players.models import (
    Players,
)


# Create your views here.
def read(request):
    try:
        players = [{'name': 'autl', 'country': 'india'}, {'name': 'asdf', 'country': 'sdafs'}]
    except:
        players = []
    print(players)
    render(request, 'index.html', {'data': players})


def form_add(request):
    render(request, 'form_add.html')


def form_update(request):
    try:
        input_player_name = request.GET['name']
        input_player_country = request.GET['country']
        render(request, 'form_update.html', {'name': input_player_name, 'country': input_player_country})
    except:
        pass


def add(request):
    input_player_name = request.GET['name']
    input_player_country = request.GET['country']
    try:
        player = Players.objects.get(name=input_player_name, country=input_player_country)
    except:
        if input_player_name and input_player_country:
            player = Players.objects.create(name=input_player_name, country=input_player_country)

    return redirect('read')


def edit(request):
    input_player_name = request.GET['name']
    input_player_country = request.GET['country']
    if input_player_country and input_player_name:
        try:
            player = Players.objects.get(name=input_player_name, country=input_player_country)
        except:
            if input_player_name and input_player_country:
                player = Players.objects.create(name=input_player_name, country=input_player_country)
    return redirect('read')


def delete(request):
    pass

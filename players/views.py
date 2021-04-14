from django.shortcuts import render, redirect
from players.models import (
    Players,
)


# Create your views here.
def read(request):
    try:
        players = Players.objects.all()
    except:
        players = []

    return render(request, 'index.html', {'players': players})


def form_add(request):
    return render(request, 'form_add.html')


def form_update(request):
    input_player_name = request.GET['name']
    input_player_country = request.GET['country']
    return render(request, 'form_update.html', {'name': input_player_name, 'country': input_player_country})


def update(request):
    prev_name = request.GET['prev_name']
    prev_country = request.GET['prev_country']
    name = request.GET['name']
    country = request.GET['country']
    if prev_country == country:
        if prev_name == name:
            return redirect('read')
    try:
        # Article.objects.filter(pk=1).update(title="New Title")
        player = Players.objects.filter(name=prev_name, country=prev_country).update(name=name, country=country)
        return redirect('read')
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
    name = request.GET['name']
    country = request.GET['country']
    Players.objects.filter(name=name,country=country).delete()
    return redirect('read')

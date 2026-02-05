from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
    search_term = request.GET.get('searchMovie')  # <- igual al name del input

    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {
        'searchTerm': search_term,
        'movies': movies
    })


def about(request):
    return HttpResponse('<h1>Welcome to the About Page</h1>')

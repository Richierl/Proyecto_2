from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Genre, Person, MovieCredit
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {'movie_list': movies}
    return render(request, "movies/index.html", context=context)

def details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie_credits = movie.moviecredit_set.all()
    context = {'movie': movie, 'movie_credits': movie_credits}
    return render(request, "movies/movie_detail.html", context=context)

def person(request, person_id):
    person = Person.objects.get(pk=person_id)
    if person.profile_path:
        base_url = ""
        profile_url = base_url + person.profile_path
    else:
        profile_url = None
    movie_credtis = MovieCredit.objects.filter(person=person)
    context = {'person': person, 'movie_credits': movie_credits, 'profile_url': profile_url}
    return render(request, 'movie/person_movies.html', context=context)
    
def genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(genres=genre)
    context = {'genre': genre, 'movies': movies}
    return render(request, 'movies/genre_movies.html', context=context)

    
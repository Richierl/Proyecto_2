from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from movies.models import Movie,Genre,Person,MovieCredit
# Create your views here.


=======
from movies.models import Movie
# Create your views here.

>>>>>>> 59204a196a74cf36b24f56af04bab945f98b84af
def index(request):
    movies = Movie.objects.all()
    context = {'movie_list': movies}
    return render(request, "movies/index.html", context=context)

<<<<<<< HEAD

def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie_credits = movie.moviecredit_set.all()  # Obtenemos las MovieCre
    context = {'movie': movie ,'movie_credits': movie_credits}
=======
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {'movie': movie}
>>>>>>> 59204a196a74cf36b24f56af04bab945f98b84af
    return render(request, "movies/movie_detail.html", context=context)

def genre_movies(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(genres=genre)
    context = {
        'genre': genre,
        'movies': movies,
    }
    return render(request, 'movies/genre_movies.html', context=context)

def person_movies(request, person_id):
    person = Person.objects.get(pk=person_id)
    if person.profile_path:
        base_url = "https://www.themoviedb.org/t/p/w300_and_h450_bestv2"
        profile_url = base_url + person.profile_path
    else:
<<<<<<< HEAD
        profile_url = None  
    movie_credits = MovieCredit.objects.filter(person=person)
    context = {'person': person, 'movie_credits': movie_credits,'profile_url': profile_url}
    return render(request, 'movies/person_movies.html', context=context)
=======
        profile_url = None
    movie_credits = MovieCredit.objects.filter(person=person)
    context = {'person': person, 'movie_credits': movie_credits,'profile_url': profile_url}
    return render(request, 'movies/person_movies.html', context=context)
>>>>>>> 59204a196a74cf36b24f56af04bab945f98b84af

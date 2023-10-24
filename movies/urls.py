from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_detail, name="movie_detail"),
<<<<<<< HEAD
]
=======
]
>>>>>>> 59204a196a74cf36b24f56af04bab945f98b84af

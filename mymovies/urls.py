from django.contrib import admin
<<<<<<< HEAD
from django.urls import include,  path
=======
from django.urls import include, path
>>>>>>> 59204a196a74cf36b24f56af04bab945f98b84af

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]

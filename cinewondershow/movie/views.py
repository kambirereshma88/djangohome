from django.shortcuts import render
from movie.models import Movies

# Create your views here.

def show_movies(request):
    result = Movies.objects.all()
    my_data = {'movie_list':result}
    return render(request,'movie/show_movies.html',context=my_data)

from django.shortcuts import render, get_object_or_404
from recosys.models import Movie
from recosys.models import User
import random
random.seed = 20


def login(request):
    return render(request, 'recosys/login.html')


def index(request):
    username = request.POST['username']
    try:
        user = User.objects.get(name=username)
        context = {'user': user}
        return render(request, 'recosys/index.html', context)
    except User.DoesNotExist:
        return render(request, 'recosys/create_user.html')


def new_user(request):
    #print(request)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(index=random.random()*10000, name=username)
    user.password = password
    user.last_name = last_name
    user.first_name = first_name
    user.email = email
    user.save()
    context = {'user': user}
    return render(request, 'recosys/index.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id) 
    return render(request, 'recosys/detail.html', {'movie': movie})

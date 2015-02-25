from django.shortcuts import render, get_object_or_404
from recosys.models import Movie
from recosys.models import User
#from django.contrib.auth import authenticate, login
#from django.http import Http404
#from django.contrib.auth.models import User
from django.shortcuts import redirect


def login(request):
    return render(request, 'recosys/login.html')


def index(request):
    username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(username=username, password=password)
    user = User.objects.get(name=username)
    if user.DoesNotExist:
            #login(request, user)
            latest_movie_list = User.objects.order_by('-date')[:10]
            context = {'user': user}
            return render(request, 'recosys/index.html', context)
    else:
        return render(request, 'recosys/create_user.html')


def new_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.last_name = last_name
    user.first_name = first_name
    user.save()
    return redirect('recosys/index.html')


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id) 
    return render(request, 'recosys/detail.html', {'movie': movie})

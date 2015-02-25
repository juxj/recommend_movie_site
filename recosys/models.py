from django.db import models
from django.utils import timezone
from jsonfield import JSONField


# Create your models here.
class MovieManager(models.Manager):
    def create_movie(self, index, name):
        movie = self.create(index=index, name=name,
                            date=timezone.now())
        return movie


class Movie(models.Model):
    index = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date released')
    rated_users = models.IntegerField(default=0)
    objects = MovieManager()

    def __str__(self):
        return self.name

    def avg_rate(self):
        total_rate = 0
        n_rate = 0
        for real_rate in self.realrate_set.all():
            total_rate += real_rate.rate
            n_rate += 1
        return n_rate, total_rate*1.0/n_rate


class UserManager(models.Manager):
    def create_user(self, index, name):
        user = self.create(index=index, name=name)
        return user


class User(models.Model):
    index = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, blank=True)
    password = models.FloatField(default=123, blank=True)
    watched_movies = models.IntegerField(default=0)
    #rated = JSONField("rated movies", blank=True, default={});
    objects = UserManager()

    def top_suggest(self):
        return self.suggestrate_set.order_by['rate'][:10]

    def rated_movies(self):
        return self.realrate_set.all().count()

    def __str__(self):
        return self.name


class RealRate(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    rate = models.FloatField()

    def __str__(self):
        return self.user.name, " rated ", self.movie.name, " as ", self.rate

    def movie_avg_rate(self):
        return "test me"


class SuggestRate(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    rate = models.FloatField()

    def __str__(self):
        return "Suggest: ", self.user.name, " rated ", self.movie.name, " as ", self.rate
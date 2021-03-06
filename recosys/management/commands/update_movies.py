__author__ = 'xju'

from django.core.management.base import BaseCommand
from recosys.models import Movie


class Command(BaseCommand):
    args = ""
    help = "Update Movie's rated users"

    def handle(self, *args, **options):
        for movie in Movie.objects.all():
            movie.rated_users = movie.realrate_set.all().count()
            movie.avg_rates = movie.avg_rate()
            movie.save()
        self.stdout.write("Successfully updated movie's rated users")

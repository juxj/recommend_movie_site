from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from recosys.models import User
from recosys.models import Movie
from recosys.models import RealRate
from recosys.models import SuggestRate


class ActiveUserListFilter(admin.SimpleListFilter):
    title = _('active users')
    parameter_name = 'user'

    def lookups(self, request, model_admin):

        return (
            ('50', _('rated 50 movies')),
            ('25', _('rated 25 movies')),
        )

    def queryset(self, request, queryset):
        try:
            n_movies = int(self.value())
            #return queryset.filter(index__in=RealRate.objects.filter(user__index))
            return queryset.filter(user__id__exact=20)
        except TypeError:
            return None


class RealRateAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rate']
    ordering = ['user']
    actions = ['active_user']
    #list_filter = (ActiveUserListFilter,)

    def active_user(self, request, queryset):
        #queryset.filter(user__realrate_set__all__count__gt=25)
        queryset.filter(rate__gt=5.0)
        self.message_user(request, "active users are successfully selected")
    active_user.short_description = "show active users"


class UserAdmin(admin.ModelAdmin):
    list_filter = (ActiveUserListFilter,)

admin.site.register(Movie)
admin.site.register(SuggestRate)
admin.site.register(User, UserAdmin)
admin.site.register(RealRate, RealRateAdmin)
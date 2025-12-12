from django.contrib import admin
from listings.models import Band, Groupe

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'biography', 'year_formed', 'active', 'officiel_homepage')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Groupe, ListingAdmin)
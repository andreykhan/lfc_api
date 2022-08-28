from django.contrib import admin
from .models import Players, Coaches


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'place_of_birth', 'age', 'position', 'number')
    search_fields = ('name', 'number')
    list_display_links = ('name',)
    list_filter = ('name',)


admin.site.register(Players, PlayersAdmin)
admin.site.register(Coaches)

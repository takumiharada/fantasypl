from django.contrib import admin

from .models import Team, League, Player

class TeamInline(admin.TabularInline):
	model = Team
	extra = 3

class LeagueInline(admin.ModelAdmin):
	inlines = [TeamInline]

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'team_name', 'totalpoints', 'cost')
	
admin.site.register(League, LeagueInline)
admin.site.register(Player, PlayerAdmin)
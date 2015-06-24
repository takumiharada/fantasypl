from django.contrib import admin

from .models import Team, League, Player

class TeamInline(admin.TabularInline):
	model = Team
	extra = 3

class LeagueInline(admin.ModelAdmin):
	inlines = [TeamInline]
	
admin.site.register(League, LeagueInline)
admin.site.register(Player)
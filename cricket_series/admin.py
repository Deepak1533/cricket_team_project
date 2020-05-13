# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cricket_series.models import (Player_History,
								   Team,
								   Player_Matchs_History,
								   Match,
								   State
								   )

# Register your models here.
@admin.register(Player_History)
class Player_HistoryAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('id', 'palyer', 'jersey_number')
	# fields = ('id', 'palyer__name', 'jersey_number')

# admin.site.register(Player_History, Player_HistoryAdmin)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('id', 'team_name')


@admin.register(Player_Matchs_History)
class Player_Matchs_HistoryAdmin(admin.ModelAdmin):
	"""docstring for Player_Matchs_HistoryAdmin"""
	list_display =('player', 'matches', 'run', 'highest', 'scores', 'fifties', 'hundreds')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
	"""docstring for MatchAdmin"""
	list_display =('id', 'get_team_one')

	def get_team_one(self, team):
		return team.team_name

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
	"""docstring for StateAdmin"""
	list_display =('id', 'state_name', 'state_code')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Team, Player_History
import json
from django.http import HttpResponse
from django.core.serializers import serialize

# Create your views here.
# class Teams(View):
# 	"""docstring for Teams"""
# 	def get(self, request, *args, **kwargs):
# 		emp_data = Team.objects.all()
# 		json_emp_data = serialize('json', emp_data)
# 		return HttpResponse(json_emp_data, content_type='application/json')

class Teams(ListView):
	"""docstring for Teams"""
	model = Team
	context_object_name = 'my_team'
	query_set = Team.objects.all()
	template = 'cricket_series/team_list.html'

	def get_context_data(self, **kwargs):
		context = super(Teams, self).get_context_data(**kwargs)
		return context

class Player_History(ListView):
	"""docstring for Teams"""
	model = Player_History
	context_object_name = 'players'
	query_set = Player_History.objects.all()
	template = 'cricket_series/player_history_list.html'

	def get_context_data(self, **kwargs):
		context = super(Player_History, self).get_context_data(**kwargs)
		return context

class Team_Players(TemplateView):
	"""docstring for Teams"""
	template_name = 'cricket_series/team_players.html'

	def get_context_data(self, **kwargs):
		from .models import Player_History
		pk = self.kwargs.get('pk', None)
		players_list = Player_History.objects.filter(team__id=pk)
		context = super(Team_Players, self).get_context_data(**kwargs)
		context['players_list'] = players_list
		return context
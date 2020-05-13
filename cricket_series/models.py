# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class State(models.Model):
	"""docstring for ClassName"""
	state_name = models.CharField(max_length=100)
	state_code = models.IntegerField(blank=True, null=True)

class Team(models.Model):
	"""docstring for ClassName"""
	team_name = models.CharField(max_length=250, blank=False)
	# identifier = models.CharField(max_length=200)
	logoUri = models.ImageField(upload_to='media', null=True, blank=True)
	club_state = models.ForeignKey(State, default=None)
	points = models.IntegerField(blank=True, default=None)

class Player_History(models.Model):
	"""docstring for Player_History"""
	palyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='palyer')
	jersey_number = models.IntegerField(blank=True)
	player_image = models.ImageField(upload_to='media', null=True, blank=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')

	def __str__(self):
		return str('%s object' %self.palyer.first_name)

class Player_Matchs_History(models.Model):
	player = models.ForeignKey(Player_History)
	matches = models.IntegerField(blank=True)
	run = models.IntegerField(blank=True)
	highest = models.IntegerField(blank=True)
	scores = models.IntegerField(blank=True)
	fifties = models.IntegerField(blank=True)
	hundreds = models.IntegerField(blank=True)

class Match(models.Model):
	"""docstring for Match"""
	team_one = models.ForeignKey(Team, default=None, related_name='team_one')
	team_two = models.ForeignKey(Team, default=None, related_name='team_two')
	winner_team = models.ForeignKey(Team, default=None, related_name='winner_team')

	def __str__(self):
		return str('%s object' % self.__class__.__name__)
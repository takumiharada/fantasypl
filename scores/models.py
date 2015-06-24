from django.db import models

class League(models.Model):
	name = models.CharField(max_length = 200)
	country = models.CharField(max_length = 200)
	league_id = models.CharField(max_length = 10)

	def __str__(self):
		return self.name
	
class Team(models.Model):
	name = models.CharField(max_length = 200)
	nickname = models.CharField(max_length = 200)
	league = models.ForeignKey(League, verbose_name = "team's league")
	team_id = models.IntegerField()
	
	def __str__(self):
		return self.name
		
class Player(models.Model):
	last_name = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 200)
	player_id = models.IntegerField()
	team_id = models.IntegerField()	
	cost = models.IntegerField()
	type_name = models.CharField(max_length = 20)
	team_name = models.CharField(max_length = 30)
	last10total = models.IntegerField()
	last10minutes = models.IntegerField()
	totalpoints = models.IntegerField()
	totalminutes = models.IntegerField()
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name		
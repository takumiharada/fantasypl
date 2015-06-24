from django.core.management.base import BaseCommand, CommandError
from scores.models import Team, League
import http.client
import json

class Command(BaseCommand):
	
	
	def handle(self, *args, **options):
		connection = http.client.HTTPConnection('api.football-data.org')
		headers = { 'X-Auth-Token': '72a15670266e4d1f93b36cfc4e45b7e2' }
		connection.request('GET', '/alpha/soccerseasons/', None, headers )
		response = json.loads(connection.getresponse().read().decode())

		for seasons in response:
			self.stdout.write(seasons['league'] + ' Number of Teams: ' + str(seasons['numberOfTeams']))
			l = League(name = seasons['caption'], league_id = seasons['league'])
			l.save()	







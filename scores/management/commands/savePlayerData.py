from django.core.management.base import BaseCommand, CommandError
from scores.models import Team, League, Player
import json, shutil, time, hashlib, glob, os

class Command(BaseCommand):
	
	
	def handle(self, *args, **options):
			
			Player.objects.all().delete()

			allplayers = json.load(open("players.current.json"))
			
			mostminutes = ""
			highestmin = 0
			
			for player in allplayers.values():
				
				totalmin = 0
			
				for match in player["fixture_history"]["all"]:
					totalmin = totalmin + match[19]
				
				count = len(player["fixture_history"]["all"]) - 1
				nummatches = 0
				
				
				totalscorelast10 = 0
				totalminuteslast10 = 0

				while nummatches < 38 and count > 0:
					if player["fixture_history"]["all"][count][3] > 0:
						totalscorelast10 = totalscorelast10 + player["fixture_history"]["all"][count][19]
						totalminuteslast10 = totalminuteslast10 + player["fixture_history"]["all"][count][3]
						nummatches = nummatches + 1
							
					count = count - 1
					
				if(player["minutes"] > 0):
					p = Player(player_id = player["id"], team_id = player["team"], last_name = player["second_name"], first_name = player["first_name"], cost = player["now_cost"], team_name = player["team_name"], totalpoints = player["total_points"], last10total = totalscorelast10, last10minutes = totalminuteslast10, type_name = player["type_name"], totalminutes = player["minutes"])
					p.save()


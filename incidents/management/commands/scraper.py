import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
from django.utils.timezone import utc

from django.core.management.base import BaseCommand, CommandError
from incidents.models import Police

class Command(BaseCommand):
	help = 'Imports incidents from City of Houston site'
	
	def handle(self, *args, **options):
		soup = BeautifulSoup(urllib2.urlopen('http://cbtcws.cityofhouston.gov/ActiveIncidents/HPDIncidents.aspx').read())
		
		for row in soup.findAll('tr',{'class': ['darkrow', 'lightrow']}):
			tds = row('td')
			address = tds[0].string
			cross_street = tds[1].string
			key_map = tds[2].string
			call_time = tds[3].string
			incident_type = tds[4].string
			combined = tds[5].string

			modified_call_time = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S').replace(tzinfo=utc)

			p, created = Police.objects.get_or_create(address=address, \
					cross_street=cross_street, \
					key_map=key_map, \
					call_time=modified_call_time, \
					incident_type=incident_type, \
					combined=combined)
			print 'Incident imported'

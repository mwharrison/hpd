from django.db import models

class Police(models.Model):
    address = models.CharField(max_length=200)
    cross_street = models.CharField(max_length=200, null=True)
    key_map = models.CharField(max_length=200, null=True)
    call_time = models.DateTimeField('date published')
    incident_type = models.CharField(max_length=200, null=True)
    combined = models.CharField(max_length=200, null=True)
    
    def __unicode__(self):
    	return ('%s (%s)') % (self.incident_type, self.address)

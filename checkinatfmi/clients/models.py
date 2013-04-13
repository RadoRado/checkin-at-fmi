from django.db import models

from places.models import Place

class Client(models.Model):
    mac = models.CharField (max_length = 63)
    status = models.NullBooleanField ()
    status_changed = models.DateTimeField (auto_now=True)
    place = models.ForeignKey (Place, null=True)
    
    def __unicode__(self):
        return "%s" % self.mac

#class Checkin(models.Model):
#    key = models.CharField(max_length = 63)
#    mac = models.CharField(max_length = 63)
#
#    def __unicode__(self):
#        return "%s checked %s" % (self.mac, self.key)

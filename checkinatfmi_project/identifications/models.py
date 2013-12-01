from django.contrib.contenttypes import generic
from django.db import models

from activities.models import Checkin


class Cardowner(models.Model):
    """
    Basic model of person with a card
    """
    carrier = generic.GenericRelation('activities.Carrier')
    faculty_number = models.IntegerField()
    grade = models.IntegerField()
    specialty = models.ForeignKey('university.Specialty')
    susi_name = models.CharField(max_length=63, null=True, blank=True)
    sudi_password = models.CharField(max_length=63, null=True, blank=True)


    @classmethod
    def register_activity(self, activity):
        print "Registering checkin for activity: " + str(activity)
        # get all active checkins for cardowner and checkout
        active_checkins = Checkin.objects.filter(checkout_activity__isnull=True)
        for checkin in active_checkins:
            checkin.checkout_activity = activity
        
        checkin.save()

    def __unicode__(self):
        return u'%s: %s' % (self.faculty_number, self.specialty)


class Book(models.Model):
    """
    Book in library
    """
    carrier = generic.GenericRelation('activities.Carrier')
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=63)

    def __unicode__(self):
        return u"%s: %s" % (self.title, self.isbn)

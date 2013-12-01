import sys
import datetime
import urllib2
import json

from django.utils.timezone import utc

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from activities.models import Checkin, Borrow
from activities.views import register_activity
from identifications.models import Book
from models import Client
from university import helper as university_helper
from university.models import Place


@csrf_exempt
@require_http_methods(['POST'])
def status(request):
    """
    Updates clients status and returns if they have the privilages to send
    """
    mac = request.POST.get("mac", "")
    client = Client.objects.get_or_create(mac = mac)[0]

    if client.status == False:
        return HttpResponse(status=401)

    client.status_changed = datetime.datetime.now()
    client.save()
    return HttpResponse(status=200)


@csrf_exempt
@require_http_methods(['POST'])
def checkin(request):
    """
    Checkin request -> asks checks
    """
    mac = request.POST.get("mac", "")
    key = request.POST.get("key", "")            
    time = request.POST.get("time", "")

    client = Client.objects.get_or_create(mac = mac)[0]
    if not client.status:
        return HttpResponse(status=401)

    print key
    #return redirect('/activities/register/', time=time, data=key, client=client)
    return register_activity(request, time=time, data=key, client=client)
    #users = CustomUser.objects.filter(card_key = key).all()
    if len(users) > 1:
        return HttpResponse("error")
    elif len(users) == 0:
        book =  get_book_or_register_user(key)
    
    user = users[0]
    if not user.valid:
        return HttpResponse("error")

    active_checkins = Checkin.objects.filter(user__first_name = user.first_name , active = True)
    for active_checkin in active_checkins:
        active_checkin.checkout(checkin_time)
    if not (client.place in [check.place for check in active_checkins]):
        print(client.place)
        Checkin.checkin(user, client.place, checkin_time)
        return HttpResponse("ok")
    return HttpResponse("error")


def rent_book(book_id, book_title):
    book, created = Book.objects.get_or_create(id=book_id, title=book_title)
    rent = Bookrent.bookrent(client.place, book, checkin_time)
    return rent

def get_book_or_register_user(key):
    response = university_helper.getBookForId(key)
    if not response:
        # There is no book for this card id
        #CustomUser.create(key)
        return False

    print(response)
    book_data = json.load(response)
    book_rent = rent_book(book_data['id'], book_data['title'])
    return book_rent

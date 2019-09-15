from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from .models import DayRating
import datetime
import json

# Create your views here.
def get_all_data(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Not logged in")
    

    responseList = []
    ratings = DayRating.objects.getRatingsForUser(request.user)


    for rating in ratings:
        responseList.append({"date" : rating.date,
                             "rating" : rating.rating,
                             "description" : rating.description, 
                             "did_submit_today" : (ratings.filter(date=datetime.date.now()) != []) 
                             })

    return JsonResponse(responseList)



def submit_rating(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Not logged in")
    data = json.loads(request.body)
    newRating = DayRating.objects.create(user=request.user, date=datetime.date.now(), description=data["description"], rating=data["rating"])
    newRating.save()
    return HttpResponse("Success")
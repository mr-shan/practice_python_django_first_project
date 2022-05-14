from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": ["Start some exercising", "Join gym", "Start cycling and running"],
    "february": ["Complete the python challenges"],
    "march": ["Finish the Django taining"],
    "april": ["Go vegan!  just kidding lol!! Reduce meat. Summery is coming"],
    "may": ["Go to vacation"],
    "june": ["Start walking for 20 mins"],
    "july": ["Start learning DSA"],
    "august": ["Consider some trading in day to day life"],
    "september": ["Start trining for cloud computing"],
    "october": ["Get certified in AWS and Azure"],
    "november": ["Start preparing for interviews"],
    "december": ["Apply to new jobs now!!"],
}

# Create your views here.


def monthly_challenge_by_number(request, month_index):
    months = list(monthly_challenges.keys())
    month_index -= 1    # The first month should be 1 not 0
    if 0 <= month_index < len(months):
        return HttpResponseRedirect("/challenges/" + months[month_index])
    else:
        return HttpResponseNotFound("404: No month found for this number")


def hello_world(request):
    return HttpResponse("Hello world from Djanog and Python world")


def monthly_challenge(request, month):
    challenge = monthly_challenges.get(month)
    if not challenge:
        return HttpResponseNotFound("404: This month is not supported")
    else:
        return HttpResponse(", ".join(challenge))

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": [],
}

# Create your views here.


def index(request):
    # index_content = "<h1>12 Months Challenge Program</h1><ul>"
    # for item in monthly_challenges:
    #     markup_href = reverse("challenges", args=[item])
    #     item_markup = f"<li><a href='{markup_href}'>{item.title()}</a></li>"
    #     index_content += item_markup
    # index_content += "</ul>"
    # return HttpResponse(index_content)
    months = monthly_challenges.keys()
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month_index):
    months = list(monthly_challenges.keys())
    month_index -= 1    # The first month should be 1 not 0
    if 0 <= month_index < len(months):
        url_redirect = reverse("challenges", args=[months[month_index]])
        print(url_redirect)
        return HttpResponseRedirect(url_redirect)
    else:
        return render(request, "challenges/404.html")


def monthly_challenge(request, month):
    challenge = monthly_challenges.get(month)
    if month not in monthly_challenges:
        return render(request, "challenges/404.html")
    else:

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        res = f"<h1>Challenges for {month.title()}</h1><ol>"
        for item in challenge:
            res += f"<li>{item}</li>"
        res += "</ol>"
        dunamic_content = {
            "month": month,
            "challenges": challenge
        }
        return render(request, "challenges/challenge.html", dunamic_content)

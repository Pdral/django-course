from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for a least 20 minutes every day!",
    "march": "Learn Django for a least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for a least 20 minutes every day!",
    "june": "Learn Django for a least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for a least 20 minutes every day!",
    "september": "Learn Django for a least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for a least 20 minutes every day!",
    "december": "Learn Django for a least 20 minutes every day!"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

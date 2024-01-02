from django.shortcuts import render
from django.http  import HttpResponse
import requests

# Create your views here.
def expeditionIndex(request):
    try:
        response=requests.get("https://www.quarkexpeditions.com/api/public/1/expedition")
        return HttpResponse(response)
    except Exception as Err:
        return HttpResponse({"message":"Please try to refresh using ctrl+ R, or, try after some time"})


def expeditionDetails(request, id):
    try:
        response = requests.get(f"https://www.quarkexpeditions.com/api/public/1/expedition/{id}")
        return HttpResponse(response)
    except requests.exceptions.RequestException as err:
        return HttpResponse(f"Error: {err}", status=500)
    
def itineraryIndex(request):
    try:
        response=requests.get("https://www.quarkexpeditions.com/api/public/1/itinerary")
        return HttpResponse(response)
    except Exception as Err:
        return HttpResponse({"message":"Please try to refresh using ctrl+ R, or, try after some time"})


def itineraryDetails(request, id):
    try:
        response = requests.get(f"https://www.quarkexpeditions.com/api/public/1/itinerary/{id}")
        return HttpResponse(response)
    except requests.exceptions.RequestException as err:
        return HttpResponse(f"Error: {err}", status=500)
    

def shipIndex(request):
    try:
        response=requests.get("https://www.quarkexpeditions.com/api/public/1/ship")
        return HttpResponse(response)
    except Exception as Err:
        return HttpResponse({"message":"Please try to refresh using ctrl+ R, or, try after some time"})


def shipDetails(request, id):
    try:
        response = requests.get(f"https://www.quarkexpeditions.com/api/public/1/ship/{id}")
        return HttpResponse(response)
    except requests.exceptions.RequestException as err:
        return HttpResponse(f"Error: {err}", status=500)
    
def cabincategoryIndex(request):
    try:
        response=requests.get("https://www.quarkexpeditions.com/api/public/1/cabin-category")
        return HttpResponse(response)
    except Exception as Err:
        return HttpResponse({"message":"Please try to refresh using ctrl+ R, or, try after some time"})


def cabincategoryDetails(request, id):
    try:
        response = requests.get(f"https://www.quarkexpeditions.com/api/public/1/cabin-category/{id}")
        return HttpResponse(response)
    except requests.exceptions.RequestException as err:
        return HttpResponse(f"Error: {err}", status=500)

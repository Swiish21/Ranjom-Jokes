import requests
from django.shortcuts import render

def index(request):
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  result = data["message"]
  return render(request, 'templates/index.html', {'result': result})

def randomJoke(request):
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  data2 = response.json()
  result1 = data2["message"]
  return render(request, 'templates/index.html', {'result': result1})
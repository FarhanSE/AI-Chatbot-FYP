from utils import testing
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'app/index.html')

def getResponse(request,msg):
    ints = testing.predict(msg)
    res = testing.det_responses(ints, testing.intents)

    return HttpResponse(f'Chatbot : {res}')
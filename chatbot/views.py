from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create your views here.

bot = ChatBot('chatbot', read_only=False, logic_adapters=[chatterbot.logic.BestMatch])


def index(request):
    return render(request, 'chatbot/index.html')


def specific(request):
    return HttpResponse('list1')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)
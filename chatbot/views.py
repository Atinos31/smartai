from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create your views here.

bot = ChatBot('chatbot', read_only=False, logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch','default_response': 'sorry , i dont know what that means','maximu_similarity_threshold':0.90
                   }])

list_to_train = [
    "Hi",
    "hi there!",
    "hey",
    "Hello there!"
    "how are you",
    "I am fine thank you, how about you?",
    "what's your name?",
    "I am just a chatbot",
    "what is your favourite food",
    "i like mac % cheese",
    "what is your favourite sport?",
    "i love to swim",
    "Do you have children?",
    "No but i would love to have afew cuties running around",
    "do you have any hobbies?",
    "duh , i love debugging"
    "bonjour",
    "bonjour cherie, tout va bien?",
    "Como estas?",
    "Estoy bien",
    "Hoi",
    "Hallo",
    "tell me a joke",
    "Helvetica and Times New Roman walk into a bar.,Get out of here! shouts the bartender. We don’t serve your type.",
    "are you a virgin",
    "well yeah , i hate plugins",
    "what is your favourite drink",
    "computers dont drink",
    "bye",
    "Goodbye!",
    "Really",
    "it's okay, chill",

]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.train.english')



def index(request):
    return render(request, 'chatbot/index.html')


def specific(request):
    return HttpResponse('list1')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
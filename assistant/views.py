import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatData

# Create your views here.
@login_required(login_url="/login")
def chat(requests):
    user = requests.user
    chat_data = user.chat_messages.all().order_by('timestamp')
    if requests.method == "POST":
        message_data = requests.POST.get("userInput")
        type = "user"
        user = requests.user
        sv_msg = ChatData.objects.create(user=user, type=type, message_data=message_data)
        response = ai_response(message_data)
        type = "ai"
        sv_response = ChatData.objects.create(user=user, type=type, message_data=response)

        return redirect("/assistant")
    
    context = {
        "chat_data":chat_data,
    }
    return render(requests, "chat.html", context=context)

def ai_response(query):
    query = str(query)
    try:
        ai_query = requests.get("https://leopard-renewing-mongoose.ngrok-free.app/query/"+query).text
    except:
        ai_query = "<!DOCTYPE html>"
    if ai_query.startswith("<!DOCTYPE html>"):
        ai_query = "Error Connecting To ai Server!!!!!"
        return ai_query
    else:
        return ai_query
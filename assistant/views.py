from django.shortcuts import render

def home(request):

    response = ""

    if request.method == "POST":

        question = request.POST.get("question")

        response = f"Vaidya AI says: {question}"

    return render(request,'index.html',{
        'response':response
    })

from django.shortcuts import render

from .ai import ask_ai

def home(request):

    response = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = ask_ai(question)

    return render(request, "index.html", {
        "response": response
    })


from django.shortcuts import render
from .ai import ask_ai

def home(request):
    response = ""

    if request.method == "POST":
        question = request.POST.get("question")
        response = ask_ai(question)

    return render(request, "index.html", {
        "response": response
    })
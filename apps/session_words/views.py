from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    words = request.session.get('words')
    context = {"words": words}
    return render(request, "session_words/index.html", context)

def add_word(request):
    if request.method == "GET":
        return render(request, "session_words/add.html")
    elif request.method == "POST":
        print request.POST
        context = {
        "date": strftime("%b %d, %Y"),
	    "time": strftime("%I:%M %p", gmtime()),
        "word": request.POST['word'],
        "color": request.POST['color'],
        "fontsize": request.POST['fontsize'],
        }
        words = request.session.get('words', [])
        words.append(context)
        request.session['words'] = words
        return redirect("index")
    
def clear(request):
    del request.session['words']
    return redirect("index")
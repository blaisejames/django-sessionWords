from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    if 'sessionid' not in request.session:
        request.session['sessionid'] = []
    print request.session['sessionid']
    return render(request, "session_words/index.html")

def add_word(request):
    if request.method == "GET":
        return render(request, "session_words/add.html")
    elif request.method == "POST":
        print request.POST
        # if request.POST['fontsize'] == 'big':
        #     size = "1.5em"
        # else:
        #     size = "1em"
        context = {
        "date": strftime("%b %d, %Y"),
	    "time": strftime("%I:%M %p", gmtime()),
        "word": request.POST['word'],
        "color": request.POST['color'],
        # "size": request.POST['fontsize'],
        "user": request.session['sessionid']
        }
        print context
        return render(request, "session_words/index.html", context)
    
def clear(request):
    del request.session['sessionid']
    return redirect("/")
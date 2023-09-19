from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.forms import RatingForm
from hello.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
    
def log_rating(request):
    form = RatingForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            rating = form.save(commit=False)
            print("rating is being saved")
            rating.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
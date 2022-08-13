from django.shortcuts import render, HttpResponse
from .models import CustomUser
from .forms import Registration
def register(request):
    req = ""
    form = Registration()
    if request.POST:
        form = Registration(request.POST)
        req = request.POST.get("full_name")
    return render(request, "register.html", {"form": form, "req": req})

from django.shortcuts import render, redirect
from .forms import DonorForm
from .models import Donor

# Create your views here.

def createDonor(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showDonor')
            except:
                pass
    else:
        form = DonorForm()
    return render(request, "Donor/donor.html", {'form': form})

def showDonor(request):
    donor = Donor.objects.all()
    return render(request, "Donor/showDonor.html", {'donor': donor})

def home(request):
    return render(request, "home.html", {})
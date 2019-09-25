from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from BBFApp.forms import *
from .forms import CustomUserCreationForm
from .filters import *

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def blood_test_method(request):
    if request.method == "POST":
        blood_testform = BloodTestForm(request.POST)
        if blood_testform.is_valid():
            try:
                blood_testform.save()
                return redirect('/show_blood_test')
            except:
                pass
    else:
        blood_testform = BloodTestForm()
    return render(request, "Test/blood_test.html", {'blood_testform': blood_testform})


def show_blood_test(request):
    blood_test_1 = BloodTest.objects.all()
    return render(request, "Test/show_blood_test.html", {'blood_test_1': blood_test_1})


def store(request):
    if request.method == "POST":
        storageform = StorageForm(request.POST)
        if storageform.is_valid():
            try:
                storageform.save()
                return redirect('/show_storage')
            except:
                pass
    else:
        storageform = StorageForm()
    return render(request, "Inventory/bag.html", {'storageform': storageform})


def show_storage(request):
    storagebags = Storage.objects.filter(available__startswith='a')
    return render(request, "Inventory/showBag.html", {'storagebags': storagebags})


def storage(request):
    storagebags = Storage.objects.filter(available__startswith='a')
    storage_filter = StorageFilter(request.GET, queryset=storagebags)
    return render(request, "Inventory/allBag.html", {'filter': storage_filter})


def create(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_donor')
            except:
                pass
    else:

        form = DonorForm()
    return render(request, "Donor/donor.html", {'form': form})


def show_donor(request):
    donate = Donor.objects.all()
    return render(request, "Donor/showDonor.html", {'donate': donate})


def edit_donor(request, reg_no):
    # d1 = Donor.objects.get(reg_no=reg_no)
    # return render(request, "Donor/editDonor.html", {'d1': d1})
    donor = Donor.objects.get(reg_no=reg_no)
    if request.method == 'POST':
        form = UpdateBloodDonorForm(request.POST, donor=donor)
        if form.is_valid():
            form.save()
            return redirect('/show_donor/')
    else:
        form = UpdateBloodDonorForm(donor=donor)
    context = {
        'form': form,
        'update': donor
    }
    return render(request, "Donor/editDonor.html", context)


def show_info(request):
    data = Donor.objects.all()
    donor_filter = DonorFilter(request.GET, queryset=data)
    return render(request, "Donor/showDonorInfo.html", {'filter': donor_filter})


def receive(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_recipient')
            except:
                pass
    else:
        form = RecipientForm()
    return render(request, "Recipient/recipient.html", {'form': form})


def show_recipient(request):
    recipients = Recipient.objects.all()
    recipient_filter = RecipientFilter(request.GET, queryset=recipients)
    return render(request, "Recipient/showRecipient.html", {'filter': recipient_filter})


def edit_bag(request, bag_id):
    bag = Storage.objects.get(bag_id=bag_id)
    if request.method == 'POST':
        form = UpdateStorageForm(request.POST, bag=bag)
        if form.is_valid():
            form.save()
            return redirect('/storage')
    else:
        form = UpdateStorageForm(bag=bag)
        context = {
            'form': form,
            'update': bag
        }
    return render(request, "Inventory/editBag.html", context)




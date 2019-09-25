from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')


# For Blood Bank
class BloodTestForm(forms.ModelForm):
    class Meta:
        model = BloodTest
        fields = "__all__"


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = "__all__"


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"
        widgets = {
            'date':forms.DateInput(attrs={'type': 'date'})
        }


class ChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = "__all__"


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"


class ConsentForm(forms.ModelForm):
    class Meta:
        model = Consent
        fields = "__all__"


class DonorInformationForm(forms.ModelForm):
    class Meta:
        model = DonorInformation
        fields = "__all__"


class PhysicalTestForm(forms.ModelForm):
    class Meta:
        model= PhysicalTest
        fields = "__all__"


class BloodDonationHistoryForm(forms.ModelForm):
    class Meta:
        model = BloodDonationHistory
        fields = "__all__"


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = "__all__"


class UpdateBloodDonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'blood_group', 'father_or_husband_name', 'age', 'gender', 'occupation', 'address', 'mobile_number']

    def save(self, commit=True):
        blood_group = self.cleaned_data.get('blood_group')
        name = self.cleaned_data.get('name')
        father_or_husband_name = self.cleaned_data.get('father_or_husband_name')
        age = self.cleaned_data.get('age')
        gender = self.cleaned_data.get('gender')
        occupation = self.cleaned_data.get('occupation')
        address = self.cleaned_data.get('address')
        mobile_number = self.cleaned_data.get('mobile_number')

        self.donor.blood_group = blood_group
        self.donor.name = name
        self.donor.father_or_husband_name = father_or_husband_name
        self.donor.age = age
        self.donor.gender = gender
        self.donor.occupation = occupation
        self.donor.address = address
        self.donor.mobile_number = mobile_number

        if commit:
            self.donor.save()
        return self.donor

    def __init__(self, *args, **kwargs):
        self.donor = kwargs.pop('donor')
        super(UpdateBloodDonorForm, self).__init__(*args, **kwargs)
        self.fields['blood_group'].initial = self.donor.blood_group
        self.fields['name'].initial = self.donor.name
        self.fields['father_or_husband_name'].initial = self.donor.father_or_husband_name
        self.fields['age'].initial = self.donor.age
        self.fields['gender'].initial = self.donor.gender
        self.fields['occupation'].initial = self.donor.occupation
        self.fields['address'].initial = self.donor.address
        self.fields['mobile_number'].initial = self.donor.mobile_number


class UpdateStorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['blood_group', 'rh_type', 'amount', 'stored_date', 'expired_date', 'available']

    def save(self, commit=True):
        blood_group = self.cleaned_data.get('blood_group')
        rh_type = self.cleaned_data.get('rh_type')
        amount = self.cleaned_data.get('amount')
        stored_date = self.cleaned_data.get('stored_date')
        expired_date = self.cleaned_data.get('expired_date')
        available = self.cleaned_data.get('available')

        self.bag.blood_group = blood_group
        self.bag.rh_type = rh_type
        self.bag.amount = amount
        self.bag.stored_date = stored_date
        self.bag.expired_date = expired_date
        self.bag.available = available
        if commit:
            self.bag.save()
        return self.bag

    def __init__(self, *args, **kwargs):
        self.bag = kwargs.pop('bag')
        super(UpdateStorageForm, self).__init__(*args, **kwargs)
        self.fields['blood_group'].initial = self.bag.blood_group
        self.fields['rh_type'].initial = self.bag.rh_type
        self.fields['amount'].initial = self.bag.amount
        self.fields['stored_date'].initial = self.bag.stored_date
        self.fields['expired_date'].initial = self.bag.expired_date
        self.fields['available'].initial = self.bag.available


class ShowListForm(forms.ModelForm):
    class Meta:
        model = DonorInformation
        fields = {'name', 'age', 'occupation', 'address', 'mobile_number'}



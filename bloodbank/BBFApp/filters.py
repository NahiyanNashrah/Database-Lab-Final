import django_filters
from .models import *


class StorageFilter(django_filters.FilterSet):
    class Meta:
        model = Storage
        fields = ['bag_id', 'blood_id', 'blood_group', 'rh_type']


class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ['reg_no', 'bag_id', 'blood_group', 'name', 'father_or_husband_name', 'age', 'gender', 'occupation', 'address', 'mobile_number']


class RecipientFilter(django_filters.FilterSet):
    class Meta:
        model = Recipient
        fields = ['serial_no', 'bag_id', 'patient_name', 'age', 'blood_group', 'gender', 'referred_by', 'ward', 'unit', 'cabin_bed', 'issue_voucher_no']




from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.email


# For Blood Bank
class BloodTest(models.Model):
    blood_id = models.CharField(primary_key=True, max_length=8)
    HCV = models.BooleanField()
    HIV = models.BooleanField()
    HBsAg = models.BooleanField()
    Syphilis = models.BooleanField()
    MP = models.BooleanField()

    class Meta:
        db_table = "blood_test"


class Storage(models.Model):
    bag_id = models.CharField(primary_key=True, max_length=8)
    blood_id = models.OneToOneField(BloodTest, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    rh_type = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=350)
    stored_date = models.DateField()
    expired_date = models.DateField()
    available = models.CharField(default='available', editable='true', max_length=20)

    class Meta:
        db_table = "storage"


class Recipient(models.Model):
    serial_no = models.IntegerField(primary_key=True, max_length=8)
    bag_id = models.ForeignKey(Storage, default=-1, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=5)
    blood_group = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    referred_by = models.CharField(max_length=50)
    ward = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    cabin_bed = models.CharField(max_length=20)
    issue_voucher_no = models.IntegerField(max_length=10)
    date = models.DateField()

    class Meta:
        db_table = "Recipient"


class Charge(models.Model):
    serial_no = models.OneToOneField(Recipient, on_delete=models.CASCADE, primary_key=True)
    whole_blood_unit = models.CharField(max_length=3)
    whole_blood_rate_per_unit = models.DecimalField(max_digits=9, decimal_places=2)
    whole_blood_amount = models.DecimalField(max_digits=14, decimal_places=2)
    crossmatch_blood_unit = models.CharField(max_length=3)
    crossmatch_blood_rate_per_unit = models.DecimalField(max_digits=9, decimal_places=2)
    crossmatch_blood_amount = models.DecimalField(max_digits=14, decimal_places=2)
    sub_total = models.DecimalField(max_digits=16, decimal_places=2)
    discount = models.DecimalField(max_digits=16, decimal_places=2)
    grand_total = models.DecimalField(max_digits=18, decimal_places=2)
    signature = models.CharField(max_length=20)

    class Meta:
        db_table = "Charge"


class Donor(models.Model):
    reg_no = models.IntegerField(primary_key=True, max_length=8)
    bag_id = models.OneToOneField(Storage, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    name = models.CharField(max_length=50, default="null")
    father_or_husband_name = models.CharField(max_length=50, default="null")
    age = models.IntegerField(max_length=8, default=0)
    gender = models.CharField(max_length=30, default="null")
    occupation = models.CharField(max_length=30, default="null")
    address = models.CharField(max_length=150, default="null")
    mobile_number = models.CharField(max_length=15, default="null")

    class Meta:
        db_table = "donor"


class Consent(models.Model):
    reg_no = models.OneToOneField(Donor, on_delete=models.CASCADE, primary_key=True)
    permitted_to_donate = models.BooleanField()
    donor_consent = models.CharField(max_length=20)
    doctor_consent = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        db_table = "Consent"


class DonorInformation(models.Model):
    reg_no = models.OneToOneField(Donor, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    father_or_husband_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=8)
    male = models.BooleanField()
    female = models.BooleanField()
    occupation = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)

    class Meta:
        db_table = "donorInformation"


class PhysicalTest(models.Model):
    reg_no = models.OneToOneField(Donor, on_delete=models.CASCADE, primary_key=True)
    weight = models.CharField(max_length=5)
    haemoglobin_level = models.CharField(max_length=8)
    bp = models.CharField(max_length=8)
    pulse = models.CharField(max_length=10)
    temp = models.CharField(max_length=5)
    heart = models.CharField(max_length=8)
    lungs = models.CharField(max_length=8)
    others = models.CharField(max_length=10)

    class Meta:
        db_table = "physical_test"


class BloodDonationHistory(models.Model):

    reg_no = models.OneToOneField(Donor, on_delete=models.CASCADE, primary_key=True)
    blood_donate_before_boolean = models.BooleanField()
    gap_of_blood_donation = models.CharField(max_length=20)
    is_recipient_relative = models.BooleanField()
    patient_name = models.CharField(max_length=50)

    class Meta:
        db_table = "blood_Donation_History"


class MedicalHistory(models.Model):
    reg_no = models.OneToOneField(Donor, on_delete=models.CASCADE, primary_key=True)
    disease_before_how_longdays = models.IntegerField(max_length=8)
    lever_disease = models.BooleanField()
    Asphyxia = models.BooleanField()
    cough = models.BooleanField()
    heart_disease = models.BooleanField()
    malaria = models.BooleanField()
    kalaazar = models.BooleanField()
    typhoid = models.BooleanField()
    operation_in_three_month = models.BooleanField()
    any_treatment_medicine_now = models.BooleanField()
    gestric = models.BooleanField()
    Haematemeses = models.BooleanField()
    blood_loo = models.BooleanField()
    rheumatic_fever = models.BooleanField()
    diabetes = models.BooleanField()
    epilepsy = models.BooleanField()
    kidney_disease = models.BooleanField()
    social_disease = models.BooleanField()
    skin_disease = models.BooleanField()
    is_blood_taken = models.BooleanField()
    is_vaccine_taken = models.BooleanField()

    class Meta:
        db_table = "medical_history"



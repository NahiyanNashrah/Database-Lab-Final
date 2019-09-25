from django.db import models

# Create your models here.

class Donor(models.Model):
    rag_no = models.AutoField(primary_key=True)
    bag_no = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    father_or_husband_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    occupation = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=20)

    class Meta:
        db_table = "donor"


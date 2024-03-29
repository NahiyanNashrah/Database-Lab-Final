# Generated by Django 2.2 on 2019-07-19 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BBFApp', '0007_consent'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorInformation',
            fields=[
                ('reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='BBFApp.Donor')),
                ('name', models.CharField(max_length=50)),
                ('father_or_husband_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=8)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('occupation', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'donorInformation',
            },
        ),
    ]

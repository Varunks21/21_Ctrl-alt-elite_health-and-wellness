# Generated by Django 4.0.6 on 2022-09-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_doctor_information_nid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='extra_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]

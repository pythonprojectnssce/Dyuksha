# Generated by Django 3.2.3 on 2021-05-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_registrationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='no_of_participants',
            field=models.CharField(max_length=3),
        ),
    ]

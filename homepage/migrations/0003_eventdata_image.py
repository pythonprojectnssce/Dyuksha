# Generated by Django 3.2.3 on 2021-05-19 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_remove_eventdata_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdata',
            name='image',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]

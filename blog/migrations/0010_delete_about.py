# Generated by Django 3.0.4 on 2020-03-26 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_about'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
    ]
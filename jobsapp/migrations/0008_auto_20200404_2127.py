# Generated by Django 2.1.7 on 2020-04-04 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0007_applicant_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='rank',
            new_name='ranks',
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Group",
            new_name="AssessmentGroup",
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-23 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_customuser_user_type_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doc_eudcation',
            new_name='doc_education',
        ),
    ]

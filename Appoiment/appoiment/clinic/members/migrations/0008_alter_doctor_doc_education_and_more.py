# Generated by Django 4.2.4 on 2023-09-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_doctor_doc_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doc_education',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doc_specialist',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Csv_File', '0002_alter_persondetail_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='aadhaar',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]

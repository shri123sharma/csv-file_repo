# Generated by Django 4.1.7 on 2023-02-22 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('New_Csv_File', '0003_alter_persondetail_aadhaar_alter_persondetail_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persondetail',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='persondetail',
            name='skill',
        ),
        migrations.AddField(
            model_name='persondetail',
            name='hobby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='New_Csv_File.hobby'),
        ),
        migrations.AddField(
            model_name='persondetail',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='New_Csv_File.skill'),
        ),
    ]
# Generated by Django 3.2.6 on 2021-11-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20211114_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='applicant',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='application',
            name='Date_of_birth',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

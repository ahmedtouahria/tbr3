# Generated by Django 4.0 on 2021-12-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbr3App', '0012_alter_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='commun',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='wilaya',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='zomra',
            field=models.CharField(max_length=3),
        ),
    ]

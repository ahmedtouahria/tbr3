# Generated by Django 4.0 on 2021-12-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbr3App', '0007_alter_person_commun_alter_person_wilaya_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='commun',
            field=models.CharField(blank=True, default='البلدية', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, default='فاعل خير', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, default='+213 ', max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='wilaya',
            field=models.CharField(blank=True, default='الولاية', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='zomra',
            field=models.CharField(blank=True, default='الزمرة', max_length=3),
        ),
    ]

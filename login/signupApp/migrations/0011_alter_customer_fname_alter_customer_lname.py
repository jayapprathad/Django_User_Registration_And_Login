# Generated by Django 4.0.2 on 2022-03-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0010_alter_customer_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lname',
            field=models.CharField(max_length=50),
        ),
    ]
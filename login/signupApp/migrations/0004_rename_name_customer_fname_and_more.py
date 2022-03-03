# Generated by Django 4.0.2 on 2022-03-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0003_alter_customer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='fname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='customer',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
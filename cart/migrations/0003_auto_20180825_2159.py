# Generated by Django 2.0.6 on 2018-08-25 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20180825_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemrequirement',
            name='product',
        ),
        migrations.RemoveField(
            model_name='itemrequirement',
            name='user',
        ),
        migrations.DeleteModel(
            name='ItemRequirement',
        ),
    ]
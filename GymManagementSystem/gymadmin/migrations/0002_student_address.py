# Generated by Django 3.0.5 on 2020-04-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
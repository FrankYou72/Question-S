# Generated by Django 3.2.5 on 2021-09-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_hardmigration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
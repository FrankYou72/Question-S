# Generated by Django 3.2.5 on 2021-08-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_customlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelList', models.JSONField()),
            ],
        ),
    ]

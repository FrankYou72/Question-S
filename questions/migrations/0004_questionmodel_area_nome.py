# Generated by Django 3.2.5 on 2021-07-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='area_nome',
            field=models.CharField(default='<django.db.models.fields.related.ForeignKey>', max_length=100),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fenster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fenster',
            name='fenster_height',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-05-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisuDados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='dado2',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

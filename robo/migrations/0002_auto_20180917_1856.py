# Generated by Django 2.1.1 on 2018-09-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='battery',
            field=models.IntegerField(default=100),
        ),
    ]
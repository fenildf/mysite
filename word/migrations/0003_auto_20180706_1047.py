# Generated by Django 2.0.4 on 2018-07-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_auto_20180705_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='collector',
        ),
        migrations.AddField(
            model_name='collector',
            name='word',
            field=models.ManyToManyField(to='word.Word'),
        ),
    ]
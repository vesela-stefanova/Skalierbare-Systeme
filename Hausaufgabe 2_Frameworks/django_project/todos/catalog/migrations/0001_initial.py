# Generated by Django 2.2.1 on 2019-05-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='todo eingeben', max_length=80)),
                ('deadline', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('progress', models.IntegerField(help_text='progress eingeben')),
            ],
        ),
    ]

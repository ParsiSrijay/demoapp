# Generated by Django 3.0.8 on 2020-08-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addpolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Policyname', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=40)),
                ('Question1', models.CharField(max_length=30)),
                ('Question2', models.CharField(max_length=30)),
                ('Question3', models.CharField(max_length=30)),
                ('Question4', models.CharField(max_length=30)),
                ('Question5', models.CharField(max_length=30)),
            ],
        ),
    ]

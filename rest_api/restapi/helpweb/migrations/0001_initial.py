# Generated by Django 3.2.13 on 2022-06-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('mno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('idweb', models.CharField(max_length=10)),
                ('passwordweb', models.CharField(max_length=20)),
                ('emailweb', models.CharField(max_length=100)),
                ('phoneweb', models.CharField(max_length=11)),
                ('addressweb', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='Notepadmdl',
            fields=[
                ('noteno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=100)),
                ('info1', models.CharField(max_length=200)),
                ('info2', models.CharField(max_length=200)),
                ('info3', models.CharField(max_length=200)),
            ],
        ),
    ]

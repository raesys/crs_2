# Generated by Django 3.1.3 on 2020-12-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camper', '0002_delete_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Dummy Model',
            },
        ),
    ]

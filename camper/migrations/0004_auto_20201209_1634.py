# Generated by Django 3.1.3 on 2020-12-09 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper', '0003_dummymodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='differentclasses',
            options={'ordering': ['name'], 'verbose_name_plural': 'Different Classes'},
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20220609_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='icon',
            field=models.CharField(blank=True, default='ideas', max_length=255, null=True),
        ),
    ]

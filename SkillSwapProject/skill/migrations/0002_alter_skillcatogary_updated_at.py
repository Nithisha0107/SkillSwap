# Generated by Django 5.0 on 2024-06-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillcatogary',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]

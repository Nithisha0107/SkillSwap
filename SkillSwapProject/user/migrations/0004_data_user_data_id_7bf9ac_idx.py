# Generated by Django 5.0 on 2024-06-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_data_user_data_name_97ceb7_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='data',
            index=models.Index(fields=['id'], name='user_data_id_7bf9ac_idx'),
        ),
    ]
# Generated by Django 2.1.5 on 2019-01-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixnet', '0004_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixnet',
            name='local_authority_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mixnet',
            name='local_decrypt_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mixnet',
            name='local_shuffle_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
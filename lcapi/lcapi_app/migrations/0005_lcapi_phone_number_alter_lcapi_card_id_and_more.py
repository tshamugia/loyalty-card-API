# Generated by Django 4.1.4 on 2023-01-15 18:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('lcapi_app', '0004_remove_lcapi_uid_alter_lcapi_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='lcapi',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='GE'),
        ),
        migrations.AlterField(
            model_name='lcapi',
            name='card_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='lcapi',
            name='surname',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_alter_user_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='saldo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

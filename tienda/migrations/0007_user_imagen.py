# Generated by Django 3.2.8 on 2021-11-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_alter_user_juegoscomprados'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='images/avatares'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-11-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawcaterapp', '0002_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]